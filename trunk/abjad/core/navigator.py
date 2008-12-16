from abjad.core.abjadcore import _Abjad
from collections import deque


### TODO profile and figure out why _Leaf.next and _Leaf.prev
###      are taking so much time

### TODO should we replace the old next with the new ._navigator._next?
###      add other next helpers such as nextLeaf?

class _Navigator(_Abjad):

   def __init__(self, client):
      self._client = client

   def _rank(self):
      '''Returns the index of the caller (its position) in 
         the parent container. If caller has no parent, 
         returns None.'''
      #if hasattr(self._client, '_parent'):
      if not self._client._parent is None:
         return self._client._parent._music.index(self._client)
      else:
         return None

   # advance to self._client._music[rank], if possible;
   # otherwise ascend
   def _advance(self, rank):
      if hasattr(self._client, '_music'):
         if rank < len(self._client._music):
            return self._client._music[rank]
         else:
            return self._client._parent
      else:
         return self._client._parent

   @property
   def _firstLeaves(self):
      '''Returns the first (leftmost) leaf or leaves 
         (in case there's a parallel structure) in a tree.'''
      if self._client.kind('_Leaf'):
         return [self._client]
      elif self._client.kind('Container'):
         leaves = [ ]
         if self._client.parallel:
            for e in self._client:
               leaves.extend(e._navigator._firstLeaves)
         else:
            #print self._client
            leaves.extend(self._client[0]._navigator._firstLeaves)
         return leaves
   
   @property
   def _lastLeaves(self):
      '''Returns the last (rightmost) leaf or leaves
         (in case there's a parallel structure) in a tree.'''
      if self._client.kind('_Leaf'):
         return [self._client]
      elif self._client.kind('Container'):
         leaves = [ ]
         if self._client.parallel:
            for e in self._client:
               leaves.extend(e._navigator._lastLeaves)
         else:
            #print self._client
            leaves.extend(self._client[-1]._navigator._lastLeaves)
         return leaves
      
   @property
   def _firstContainers(self):
      '''Returns the first (leftmost) container or containers 
         (in case there's a parallel structure) in the calling structure.'''
      if self._client.kind('Container'):
         containers = [ ]
         if self._client.parallel:
            for e in self._client:
               containers.extend(e._navigator._firstContainers)
         else:
            containers.append(self._client)
         return containers
      else:
         return [None]

   @property
   def _contemporaneousContents(self):
      '''Leaf: returns [self].
         Container: returns list of every component in self
         that starts at the same moment as self (including self).

         Intuitively: starts at self and then burrows all the way 
         down the score tree to return a list of everything inside
         of self starting at the same moment as self.'''
      result = [ ]
      client = self._client
      result.append(client)
      if client.kind('Container'):
         if client.parallel:
            for x in client:
               result.extend(x._navigator._contemporaneousContents)
         else:
            result.extend(client[0]._navigator._contemporaneousContents)
      return result
   
   @property
   def _nextLeaves(self):
      '''Returns list of next leaf/leaves regardless of "thread" or type 
         of caller. If next component is/contains a parallel, return list 
         of simultaneous leaves'''
      next = self._next
      if next:
         firstleaves = next._navigator._firstLeaves
         return firstleaves

   @property
   def _prevLeaves(self):
      '''Returns list of previous leaf/leaves regardless of "thread" or type 
         of caller. If next component is/contains a parallel, return list 
         of simultaneous leaves'''
      prev = self._prev
      if prev:
         lastLeaves = prev._navigator._lastLeaves
         return lastLeaves

   @property
   def _nextSibling(self):
      '''Returns the next *sequential* element in the caller's parent; 
         None otherwise'''
      rank = self._rank( )
      if (not rank is None) and (not self._client._parent.parallel): 
      # (parallels are siameses)
         if rank + 1 < len(self._client._parent._music):
            return self._client._parent._music[rank + 1]
      else:
         return None
         
   @property
   def _prevSibling(self):
      '''Returns the previous *sequential* element in the caller's parent; 
         None otherwise'''
      rank = self._rank( )
      if (not rank is None) and (not self._client._parent.parallel): 
      # (parallels are siameses)
         if rank - 1 >= 0:
            return self._client._parent._music[rank - 1]
      else:
         return None

   @property
   def _next(self):
      '''Returns next closest non-siamese Component.'''
      next = self._nextSibling
      if next:
         return next
      else:
         for p in self._client._parentage._parentage:
            next = p._navigator._nextSibling
            if next:
               return next
      
   @property
   def _prev(self):
      '''Returns previous closest non-siamese Component.'''
      prev = self._prevSibling
      if prev:
         return prev
      else:
         for p in self._client._parentage._parentage:
            prev = p._navigator._prevSibling
            if prev:
               return prev
      
   @property
   def _nextBead(self):
      '''Returns the next Bead (time threaded Leaf), if such exists. 
         This method will search the whole (parentage) structure moving forward.
         This will only return if called on a Leaf.'''
      if not self._client.kind('_Leaf'):
         return None
      next = self._next
      if next is None:
         return None
      candidates = next._navigator._firstLeaves
      return self._findFellowBead(candidates)

   @property
   def _prevBead(self):
      '''Returns the previous Bead (time threaded Leaf), if such exists. 
         This method will search the whole (parentage) structure moving back.
         This will only return if called on a Leaf.'''
      if not self._client.kind('_Leaf'):
         return None
      prev = self._prev
      if prev is None:
         return None
      candidates = prev._navigator._lastLeaves
      return self._findFellowBead(candidates)

   @property
   def _nextThread(self):
      '''Returns the next threadable Container.'''
      if not self._client.kind('Container'):
         return None
      next = self._next
      if next is None or next.kind('_Leaf'):
         return None
      containers = next._navigator._firstContainers
      for c in containers:
         if not c is None:
            if self._isThreadable(c):
               return c

   def _getImmediateTemporalSuccessors(self):
      cur = self._client
      while cur is not None:
         nextSibling = cur._navigator._nextSibling
         if nextSibling is None:
            cur = cur._parent
         else:
            return nextSibling._navigator._contemporaneousContents
      return [ ]

   def _isImmediateTemporalSuccessorOf(self, expr):
      return expr in self._getImmediateTemporalSuccessors( )
         
   def _isThreadable(self, expr):
      '''Check if expr is threadable with respect to self.'''
      c_thread_parentage = expr._parentage._threadParentage
      thread_parentage = self._client._parentage._threadParentage
      match_parent = True
      if len(c_thread_parentage) == len(thread_parentage):
         for c, p in zip(c_thread_parentage, thread_parentage):
            if type(c) == type(p):
               if c.kind('_Context') and p.kind('_Context'):
                  if c.invocation != p.invocation:
                     match_parent = False
      else:
         match_parent = False
      match_self = False
      if self._client.kind('_Leaf') and expr.kind('_Leaf'):
         match_self = True
      elif self._client.kind('Container') and expr.kind('Container'):
         if not self._client.parallel and not expr.parallel:
            if self._client.kind('_Context') and expr.kind('_Context'):
               if self._client.invocation == expr.invocation:
                  match_self =  True
            elif type(self._client) == type(expr):
               match_self =  True
      return match_self and match_parent

   def _pathExistsBetween(self, arg):
      '''Returns True when self._client and arg are ultimately contained
         in the same expression, when a reference pathway exists between
         self._client and arg that passes over no \new or \context
         boundaries, and when a reference path exists between self._client
         and arg that crosses over no parallel containers.
         
         I propose replacing _isThreadable with this method.'''
      return self._hasGoodSharedParent(arg) and self._hasGoodPath(arg)

   def _hasGoodSharedParent(self, arg):
      '''Returns True when self._client and arg have at least one
         element of shared parentage and the first element of shared
         parentage between self._client and arg is not parallel.'''
      first_shared = self._client._parentage._getFirstSharedParent(arg)
      return first_shared and not first_shared.parallel

   def _isInaccessibleToMe(self, arg):
      return getattr(arg, 'parallel', False) or \
         (hasattr(arg, 'invocation') and not self._shareContext(arg)) or \
         (hasattr(arg, 'invocation') and arg.invocation.name is None)

   def _shareContext(self, arg):
      '''Return True when self._client and arg share the same
         enclosing context name, otherwise False.'''
      return self._client._parentage._enclosingContextName == \
         arg._parentage._enclosingContextName

   def _hasGoodPath(self, arg):
      '''Returns True when all of the disjunct elements in the parentage
         of self._client and arg share the same context and when none
         of the disjunct elements in the parentage of self._client and arg
         are parallel containers.'''
      parentage = \
         self._client._parentage._disjunctInclusiveParentageBetween(arg)
      return not any([self._isInaccessibleToMe(p) for p in parentage])
      
   def _findFellowBead(self, candidates):
      '''Helper method from prevBead and nextBead. 
      Given a list of bead candiates of self, find and return the first one
      that matches thread parentage. '''
      for candidate in candidates:
         if self._isThreadable(candidate):
            return candidate
#         c_thread_parentage = candidate._parentage._threadParentage
#         thread_parentage = self._client._parentage._threadParentage
#         #print thread_parentage
#         #print c_thread_parentage
#         ### check that parentages match.
#         match = True
#         if len(c_thread_parentage) == len(thread_parentage):
#            for c, p in zip(c_thread_parentage, thread_parentage):
#               if type(c) == type(p):
#                  #if c.kind('Context') and p.kind('Context'):
#                  if c.kind('_Context') and p.kind('_Context'):
#                     if c.invocation != p.invocation:
#                        match = False
#         else:
#            match = False
#
#         if match:
#            return candidate

   # rightwards depth-first traversal:
   # advance rightwards; otherwise ascend; otherwise None.
   # return next node yet-to-be visited, last rank already visited
   def _nextNodeHelper(self, lastVisitedRank = None):
      if hasattr(self._client, '_music'):
         if lastVisitedRank is None:
            if len(self._client._music) > 0:
               return self._client._music[0], None
            else:
               return None, None
         else:
            if lastVisitedRank + 1 < len(self._client._music):
               return self._client._music[lastVisitedRank + 1], None
            elif self._client._parent:
               return self._client._parent, self._rank( )
            else:
               return None, None
      elif self._client._parent:
         return self._client._parent, self._rank( )
      else:
         return None, None

   # leftwards depth-first traversal;
   # return next node yet-to-be visited, last rank already visited
   def _prevNodeHelper(self, lastVisitedRank = None):
      if hasattr(self._client, '_music'):
         if lastVisitedRank == None:
            if len(self._client._music) > 0:
               return self._client._music[-1], None
            else:
               return None, None
         else:
            if lastVisitedRank > 0:
               return self._client._music[lastVisitedRank - 1], None
            elif self._client._parent:
               return  self._client._parent, self._rank( )
            else:
               return None, None
      elif not hasattr(self._client, '_parent'):
         print 'WARNING: node without parent!'
         print self._client.lily
         print ''
         raise Exception
      elif self._client._parent:
         return self._client._parent, self._rank( )
      else:
         return None, None

#   def _traverse(self, v):
#      v.visit(self._client)
#      if hasattr(self._client, '_music'):
#         for m in self._client._music:
#            m._navigator._traverse(v)
#      if hasattr(v, 'unvisit'):
#         v.unvisit(self._client)

   def _traverse(self, v, depthFirst=True, leftRight=True):
      if depthFirst:
         self._traverseDepthFirst(v)
      else:
         self._traverseBreadthFirst(v, leftRight)

   def _traverseDepthFirst(self, v):
      v.visit(self._client)
      if hasattr(self._client, '_music'):
         for m in self._client._music:
            m._navigator._traverse(v)
      if hasattr(v, 'unvisit'):
         v.unvisit(self._client)

   def _traverseBreadthFirst(self, v, leftRight = True):
      queue = deque([self._client])
      while queue:
         node = queue.popleft( )
         v.visit(node)
         if hasattr(node, '_music'):
            if leftRight:
               queue.extend(node._music)
            else:
               queue.extend(reversed(node._music))

   def _nextNodeDF(self, total):
      '''
      If client has unvisited music, 
      return next unvisited node in client's music.

      If client has no univisited music and has a parent,
      return client's parent.

      If client has no univisited music and no parent,
      return None.
      '''

      client = self._client
      if hasattr(client, '_music') and len(client) > 0 and \
         total < len(client):
         return client[total], 0 
      else:
         parent = client._parent
         if parent is not None:
            return parent, parent.index(client) + 1
         else:
            return None, None

   def _prevNodeDF(self, total = 0):
      '''
      If client has unvisited music, 
      return prev unvisited node in client's music.

      If client has no univisited music and has a parent,
      return client's parent.

      If client has no univisited music and no parent,
      return None.
      '''

      client = self._client
      if hasattr(client, '_music') and len(client) > 0 and \
         total < len(client):
         return client[len(client) - 1 - total], 0
      else:
         parent = client._parent
         if parent is not None:
            return parent, len(parent) - parent.index(client)
         else:
            return None, None

   def _depthFirstLeftToRight(self):
      node, rank = self._client, 0 
      while node is not None:
         yield node
         node, rank = node._navigator._nextNodeDF(rank)

   def _depthFirstRightToLeft(self):
      node, total = self._client, 0
      while node is not None:
         yield node
         node, total = node._navigator._prevNodeDF(total)

#   def _levelDFRL(self):
#      node, total, level = self._client, 0, 0
#      while node is not None:
#         yield node, level
#         node, total, level = node._navigator._prevNodeLevelDF(total, level)
#
#   def _prevNodeLevelDF(self, total = 0, level = 0):
#      '''
#      Like _prevNodeDF( ) but returns (component, level) pairs
#      where level is an integer describing the level of component
#      in relation to client, with 0 equal to the level of client,
#      -1 equalling the level lower than client, +1 equalling
#      the level higher than client, etc.
#      '''
#
#      client = self._client
#      if hasattr(client, '_music') and len(client) > 0 and \
#         total < len(client):
#         return client[len(client) - 1 - total], 0, level - 1
#      else:
#         parent = client._parent
#         if parent is not None:
#            return parent, len(parent) - parent.index(client), level + 1
#         else:
#            return None, None, None

   def _cappedDFSLeft(self):
      parent, node, rank = self._client._parent, self._client, 0 
      while node is not parent:
         yield node
         node, rank = node._navigator._nextNodeDF(rank)

   def _cappedDFSRight(self):
      parent, node, rank = self._client._parent, self._client, 0 
      while node is not parent:
         yield node
         node, rank = node._navigator._prevNodeDF(rank)

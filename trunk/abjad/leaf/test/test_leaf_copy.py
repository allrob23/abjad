from abjad import *


### TEST COPY ONE LEAF ###

def test_leaf_copy_01( ):
   m = Note(0, (1, 8))
   n = componenttools.clone_components_and_fracture_crossing_spanners([m])[0]
   assert id(m) != id(n)
   assert m.parentage.parent is None
   assert n.parentage.parent is None


def test_leaf_copy_02( ):
   r = Rest((1, 8))
   s = componenttools.clone_components_and_fracture_crossing_spanners([r])[0]
   assert id(r) != id(s)
   assert r.parentage.parent is None
   assert s.parentage.parent is None


def test_leaf_copy_03( ):
   s = Skip((1, 8))
   t = componenttools.clone_components_and_fracture_crossing_spanners([s])[0]
   assert id(s) != id(t)
   assert s.parentage.parent is None
   assert t.parentage.parent is None


def test_leaf_copy_04( ):
   d = Chord([2, 3, 4], (1, 4))
   e = componenttools.clone_components_and_fracture_crossing_spanners([d])[0]
   assert id(d) != id(e)
   assert d.parentage.parent is None
   assert e.parentage.parent is None


def test_leaf_copy_05( ):
   t = FixedDurationTuplet((1, 4), Note(0, (1, 8)) * 3)
   m = t[1]
   n = componenttools.clone_components_and_fracture_crossing_spanners([m])[0]
   assert id(m) != id(n)
   assert m.parentage.parent is t
   assert n.parentage.parent is None


### TEST COPY ONE CONTAINER ###

def test_leaf_copy_06( ):
   t = Staff([Note(n, (1, 8)) for n in range(8)])
   u = componenttools.clone_components_and_fracture_crossing_spanners([t])[0]
   id(u) is not id(t)
   check.wf(t)
   check.wf(u)


### TEST COPY ONE TUPLETIZED NOTE ###

def test_leaf_copy_07( ):
   t = Staff(FixedDurationTuplet((2, 8), Note(0, (1, 8)) * 3) * 3)
   u = componenttools.clone_components_and_fracture_crossing_spanners(t.leaves[4:5])[0]
   assert isinstance(u, Note)
   assert u.pitch.number == t.leaves[4].pitch.number
   assert u.duration.written == t.leaves[4].duration.written
   assert id(u) != id(t.leaves[4])
   assert u.duration.prolated != t.leaves[4].duration.prolated


def test_leaf_copy_08( ):
   t = Staff(FixedDurationTuplet((2, 8), Note(0, (1, 8)) * 3) * 3)
   u = componenttools.clone_components_and_fracture_crossing_spanners(t.leaves[5:6])[0]
   assert isinstance(u, Note)
   assert u.pitch.number == t.leaves[5].pitch.number
   assert u.duration.written == t.leaves[5].duration.written
   assert id(u) != id(t.leaves[5])
   assert u.duration.prolated != t.leaves[5].duration.prolated

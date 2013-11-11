#!/usr/bin/python2
# coding: utf-8

def splitList(list_, chunksize = 2):
  return [list_[i:i + chunksize] for i in xrange(0, len(list_), chunksize)]

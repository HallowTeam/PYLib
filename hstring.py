#!/usr/bin/python2
# coding: utf-8

def splitStr(string, size = 2):
  return [string[i:i + size] for i in xrange(0, len(string), size)]


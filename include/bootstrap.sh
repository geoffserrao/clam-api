#!/bin/bash
freshclam && freshclam -d
clamd --foreground

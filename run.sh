#!/bin/bash
pytest --tb=no --json-report > test.log
cat .report.json
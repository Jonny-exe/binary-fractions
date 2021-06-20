#!/usr/bin/bash

#
cnt=$(grep "# autogenerate README.md" .git/hooks/pre-commit.sample | wc -l)
if [ "$cnt" == "2" ]; then
  return
fi
echo "" >> .git/hooks/pre-commit.sample 
echo "# autogenerate README.md" >> .git/hooks/pre-commit.sample 
echo "pydoc-markdown -I ../../binary_fractions/ -m binary --render-toc > ../../binary_fractions/ README.md" >> .git/hooks/pre-commit.sample 
echo "echo 'Generated new Documents'" >> .git/hooks/pre-commit.sample 

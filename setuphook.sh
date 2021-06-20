#!/usr/bin/bash

#
cnt=$(grep "# autogenerate README.md" .git/hooks/pre-commit | wc -l)
if [ "$cnt" == "2" ]; then
  return
fi
echo "" >> .git/hooks/pre-commit
echo "# autogenerate README.md" >> .git/hooks/pre-commit
echo "pydoc-markdown -I ../../binary_fractions/ -m binary --render-toc > ../../binary_fractions/ README.md" >> .git/hooks/pre-commit
echo "echo 'Generated new Document README.md'" >> .git/hooks/pre-commit

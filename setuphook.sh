#!/usr/bin/bash

#
# This file is only needed by developers who want to automatically generate
# the API documentation when performing a `git push`.
# This sets up a git hook on the local machine of the developer which
# triggers that on each `git push` a new API document is auto-generated in
# markdown format using pydoc and the pydoc-markdown tools.
# This auto-generated file is binary_fractions/README.md.
#

HOOKFILE=".git/hooks/pre-commit"
PATTERN="# autogenerate README.md"

if ! test -f "$HOOKFILE"; then
  echo "Copying file from \"${HOOKFILE}.sample\" to \"$HOOKFILE\"."
  cp "${HOOKFILE}.sample" "$HOOKFILE"
else
  echo "${HOOKFILE} already exists. Perfect."
fi

cnt=$(grep "$PATTERN" $HOOKFILE | wc -l)
if [ "$cnt" == "0" ]; then
  #
sed -i "s/# Cross platform projects tend to avoid non-ASCII filenames; prevent/\n\n$PATTERN\npydoc-markdown -I .\/binary_fractions -m binary --render-toc  > .\/binary_fractions\/README.md\necho Generated new document README.md\npython3 update_readme.py\n.\/update_version.sh\ngit add binary_fractions/binary.py\ngit add README.md\n\n# Cross platform projects tend to avoid non-ASCII filenames; prevent/" $HOOKFILE
  echo "Modified file $HOOKFILE"
else
  echo "Nothing to do, setup was already done in $HOOKFILE"
fi
# EOF

#!/usr/bin/bash

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
  sed -i "s/# Cross platform projects tend to avoid non-ASCII filenames; prevent/\n\n$PATTERN\npydoc-markdown -I .\/binary_fractions -m binary --render-toc  > .\/binary_fractions\/README.md\necho Generated new document README.md\n\n\n# Cross platform projects tend to avoid non-ASCII filenames; prevent/" $HOOKFILE
  echo "Modified file $HOOKFILE"
else
  echo "Nothing to do, setup was already done in $HOOKFILE"
fi
# EOF

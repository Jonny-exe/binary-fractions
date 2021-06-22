#!/usr/bin/bash

#
# This file is only needed by developers who want to automatically generate
# the API documentation when performing a `git push`.
# This sets up a git hook on the local machine of the developer which
# triggers that on each `git push` a new API document is auto-generated in
# markdown format using pydoc and the pydoc-markdown tools.
# This auto-generated file is binary_fractions/README.md.
#

PATTERN="_BINARY_VERSION ="
SOURCEFILE="binary_fractions/binary.py"
SEDPATTERN="$PATTERN \"[0-9]*-[0-9]*\""

if ! test -f "$SOURCEFILE"; then
  echo "File \"$SOURCEFILE\"not found."
else
  echo "${SOURCEFILE} found. Perfect."
fi

cnt=$(grep "$PATTERN" $SOURCEFILE | wc -l)
if [ "$cnt" == "1" ]; then
  #
  VERSION="_BINARY_VERSION = \"$(date +%Y%m%d-%H%M%S)\""
  # echo "THIS IS THE VERSION $VERSION"
  sed -i "s/$SEDPATTERN/$VERSION/" $SOURCEFILE
  ret=$?
  if [ "$ret" == "0" ]; then
    echo "Modified file $SOURCEFILE by setting version to $VERSION."
  else
    echo "ERROR: could not change version to $VERSION in $SOURCEFILE."
  fi
else
  echo "ERROR: Version not found, or too many versions found."
fi
# EOF

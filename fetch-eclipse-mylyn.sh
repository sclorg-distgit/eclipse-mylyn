#!/bin/sh

set -e

RELEASE_TAG="R_3_18_0"
FETCHED_SOURCES_NAME="eclipse-mylyn-${RELEASE_TAG}-fetched-src"

#clean up old runs
rm -rf $FETCHED_SOURCES_NAME

#checkout
git clone --recursive git://git.eclipse.org/gitroot/mylyn/org.eclipse.mylyn.all.git $FETCHED_SOURCES_NAME
cd $FETCHED_SOURCES_NAME
git checkout $RELEASE_TAG
git submodule update

#remove precomipled binaries
find . -type f -name ".class" -exec rm {} \;
find . -type f -name ".jar" -exec rm {} \;
rm -rf .git
find . -type f -name ".gitignore" -exec rm {} \;
find . -type f -name ".gitmodules" -exec rm {} \;

cd ..

#package and clean up
tar -caf $FETCHED_SOURCES_NAME.tar.xz $FETCHED_SOURCES_NAME
rm -rf $FETCHED_SOURCES_NAME

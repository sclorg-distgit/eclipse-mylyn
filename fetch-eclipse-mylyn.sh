#!/bin/sh

set -e

RELEASE_TAG="R_3_14_2"
FETCHED_SOURCES_NAME="eclipse-mylyn-${RELEASE_TAG}-fetched-src"

#clean up old runs
rm -rf org.eclipse.mylyn.all
rm -rf $FETCHED_SOURCES_NAME
rm -rf $RELEASE_TAG

#checkout
git clone --recursive git://git.eclipse.org/gitroot/mylyn/org.eclipse.mylyn.all.git $RELEASE_TAG
cd $RELEASE_TAG
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
mv $RELEASE_TAG $FETCHED_SOURCES_NAME
tar -caf $FETCHED_SOURCES_NAME.tar.xz $FETCHED_SOURCES_NAME
rm -rf $FETCHED_SOURCES_NAME

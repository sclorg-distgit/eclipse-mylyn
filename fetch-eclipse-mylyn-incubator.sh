#!/bin/sh

set -e

RELEASE_TAG="4c800cb4e89aab31590a96fe961d56464d54383b"
FETCHED_SOURCES_NAME="eclipse-mylyn-${RELEASE_TAG}-incubator-fetched-src"

#clean up old runs
rm -rf $FETCHED_SOURCES_NAME

#checkout
git clone git://git.eclipse.org/gitroot/mylyn/org.eclipse.mylyn.incubator.git $FETCHED_SOURCES_NAME
cd $FETCHED_SOURCES_NAME
git checkout $RELEASE_TAG

#remove projects we do not need
ls -1 | grep -v  -e "org.eclipse.mylyn.trac.wiki-feature" \
    -e "org.eclipse.mylyn.trac.wiki" \
    -e "org.eclipse.mylyn.web.tasks-feature" \
    -e "org.eclipse.mylyn.web.tasks" | xargs rm -rf

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

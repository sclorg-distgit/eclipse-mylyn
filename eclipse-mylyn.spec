%{?scl:%scl_package eclipse-mylyn}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global baserelease 4

%global tag R_3_18_0
%global incubator_tag 4ed20a19954cfd37d6575da179cfe7b1fae0a465

%if 0%{?fedora} >= 24
%global droplets droplets
%else
%global droplets dropins
%endif

Name:    %{?scl_prefix}eclipse-mylyn
Summary: Eclipse Mylyn main feature.
Version: 3.18.0
Release: 5.%{baserelease}%{?dist}
License: EPL
URL: http://www.eclipse.org/mylyn

# bash fetch-eclipse-mylyn.sh
Source0: eclipse-mylyn-%{tag}-fetched-src.tar.xz
Source1: fetch-eclipse-mylyn.sh
Source6: redhat-bugzilla-custom-transitions.txt
Source7: eclipse-mylyn-%{incubator_tag}-incubator-fetched-src.tar.xz
Source8: fetch-eclipse-mylyn-incubator.sh 

Patch0: %{pkg_name}-remove-hudson-discovery.patch
Patch1: %{pkg_name}-add-apache-xmlrpc.patch
Patch2: %{pkg_name}-disable-online-tests.patch
Patch3: %{pkg_name}-merge-incubator.patch
Patch4: %{pkg_name}-bug-419133.patch
%if 0%{?fedora} == 22
Patch5: lucene4.patch
%else
Patch5: 0001-Compile-with-Lucene-5.patch
%endif
Patch6: %{pkg_name}-remove-nullable-annotation.patch
Patch7: explicit-hamcrest-use.patch
Patch8: %{pkg_name}-bree-bump.patch
Patch9: eclipse-fix-bugzilla-and-versions-tests.patch

BuildArch: noarch

BuildRequires: %{?scl_prefix}eclipse-pde >= 1:4.2.0
BuildRequires: %{?scl_prefix}eclipse-cdt
BuildRequires: %{?scl_prefix}eclipse-egit
BuildRequires: %{?scl_prefix}eclipse-jgit
BuildRequires: %{?scl_prefix}eclipse-license
BuildRequires: %{?scl_prefix}eclipse-emf
BuildRequires: %{?scl_prefix}tycho
BuildRequires: %{?scl_prefix}eclipse-egit
BuildRequires: %{?scl_prefix_java_common}lucene5
BuildRequires: %{?scl_prefix_java_common}lucene5-queryparser
BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: %{?scl_prefix_java_common}apache-commons-lang >= 2.6-6
BuildRequires: %{?scl_prefix_java_common}apache-commons-logging
BuildRequires: %{?scl_prefix_java_common}apache-commons-io >= 2.3
BuildRequires: %{?scl_prefix_java_common}ws-commons-util >= 1.0.1-21
BuildRequires: %{?scl_prefix_java_common}xmlrpc-client >= 3.1.3
BuildRequires: %{?scl_prefix_java_common}xmlrpc-common >= 3.1.3
BuildRequires: %{?scl_prefix_java_common}xmlrpc-server >= 3.1.3
BuildRequires: %{?scl_prefix}rome >= 0.9-9
BuildRequires: %{?scl_prefix_java_common}httpcomponents-client
BuildRequires: %{?scl_prefix_java_common}httpcomponents-core
BuildRequires: %{?scl_prefix_java_common}google-gson >= 2.0.0
BuildRequires: %{?scl_prefix}guava
BuildRequires: %{?scl_prefix_java_common}xalan-j2
BuildRequires: %{?scl_prefix_java_common}junit
BuildRequires: %{?scl_prefix_java_common}hamcrest
BuildRequires: %{?scl_prefix_java_common}objenesis
BuildRequires: %{?scl_prefix}mockito >= 1.10.19-3.7
BuildRequires: %{?scl_prefix_maven}maven-deploy-plugin
BuildRequires: %{?scl_prefix_maven}maven-plugin-build-helper
BuildRequires: %{?scl_prefix_maven}xml-maven-plugin
BuildRequires: %{?scl_prefix}tika
BuildRequires: %{?scl_prefix}tika-parsers
BuildRequires: %{?scl_prefix}jsoup

Requires:      %{?scl_prefix}eclipse-platform

# Obsoletes/Provides added in F22
Obsoletes: %{name}-ide < %{version}-%{release}
Provides:  %{name}-ide = %{version}-%{release}
Obsoletes: %{name}-context-team < %{version}-%{release}
Provides:  %{name}-context-team = %{version}-%{release}

%description
Mylyn integrates task support into Eclipse. It supports offline editing
for certain task repositories and monitors work activity to hide
information that is not relevant to the current task.

%package context-java
Summary:  Mylyn Bridge:  Java Development
Requires: %{?scl_prefix}eclipse-jdt

%description context-java
Mylyn Task-Focused UI extensions for JDT.  Provides focusing of Java
element views and editors.

%package context-pde
Summary:  Mylyn Bridge:  Plug-in Development
Requires: %{?scl_prefix}eclipse-pde

%description context-pde
Mylyn Task-Focused UI extensions for PDE, Ant, Team Support and CVS.

%package context-cdt
Summary:  Mylyn Bridge:  C/C++ Development
Requires: %{?scl_prefix}eclipse-cdt

%description context-cdt
Mylyn Task-Focused UI extensions for CDT.  Provides focusing of C/C++
element views and editors.

%package tasks-bugzilla
Summary: Mylyn Tasks Connector: Bugzilla

%description tasks-bugzilla
Provides Task List integration, offline support and rich editing for the
open source Bugzilla bug tracker.

%package docs-wikitext
Summary: Mylyn WikiText
Obsoletes: %{name}-docs-htmltext < %{version}-%{release}
Provides:  %{name}-docs-htmltext = %{version}-%{release}

%description docs-wikitext
Enables parsing and display of lightweight markup (wiki text) and HTML text.

%package docs-epub
Summary: Mylyn EPub

%description docs-epub
The EPUB framework in Mylyn Docs offers API to create, manipulate,
read and write EPUB formatted files. 

%package  tasks-trac
Summary: Mylyn Tasks Connector: Trac

%description tasks-trac
Provides Task List integration, offline support and rich editing
for the open source Trac issue tracker.

%package  tasks-web
Summary: Mylyn Tasks Connector: Web Templates (Advanced) (Incubation)

%description tasks-web
Provides Task List integration for web-based issue trackers
and templates for example projects.

%package versions
Summary: Eclipse Mylyn Versions

%description versions
Provides a framework for accessing team providers for Eclipse Mylyn.

%package versions-git
Summary: Mylyn Versions Connector: Git

%description versions-git
Provides Git integration for Eclipse Mylyn.

%package versions-cvs
Summary: Mylyn Versions Connector: CVS

%description versions-cvs
Provides CVS integration for Eclipse Mylyn.

%package builds
Summary: Eclipse Mylyn Builds

%description builds
Provides a common framework to interact with continuous integration
build providers using Eclipse Mylyn.

%package builds-hudson
Summary: Mylyn Builds Connector: Hudson/Jenkins

%description builds-hudson
Support for the open source Hudson and Jenkins continuous integration servers.

%package sdk
Summary: Mylyn SDK
Requires: %{name} = %{version}-%{release}
Requires: %{name}-builds = %{version}-%{release}
Requires: %{name}-builds-hudson = %{version}-%{release}
Requires: %{name}-context-cdt = %{version}-%{release}
Requires: %{name}-context-java = %{version}-%{release}
Requires: %{name}-context-pde = %{version}-%{release}
Requires: %{name}-docs-epub = %{version}-%{release}
Requires: %{name}-docs-wikitext = %{version}-%{release}
Requires: %{name}-tasks-bugzilla = %{version}-%{release}
Requires: %{name}-tasks-trac = %{version}-%{release}
Requires: %{name}-tasks-web = %{version}-%{release}
Requires: %{name}-versions = %{version}-%{release}
Requires: %{name}-versions-cvs = %{version}-%{release}
Requires: %{name}-versions-git = %{version}-%{release}

%description sdk
Sources for all Mylyn bundles.

%package tests
Summary: Mylyn test bundles
Requires: %{?scl_prefix}eclipse-tests
Requires: %{?scl_prefix}eclipse-swtbot
Requires: %{?scl_prefix}mockito >= 1.10.19-3.7

%description tests
All the test bundles for mylyn packages.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%setup -q -n eclipse-mylyn-%{tag}-fetched-src
tar xaf %{SOURCE7} -C org.eclipse.mylyn.tasks --strip-components=1

%patch0
%patch1
%patch2 -b .sav
%patch3 -b .sav
%patch4
pushd org.eclipse.mylyn.tasks
%patch5 -p1 -b .sav
popd
%patch6
%patch7
pushd org.eclipse.mylyn.tasks
%patch8 -p1
popd
%patch9

#remove tests that fail to compile
rm -rf org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.ui.tests/src/org/eclipse/mylyn/commons/ui/ShellDragSupportTest.java
rm -rf org.eclipse.mylyn.builds/org.eclipse.mylyn.hudson.ui/src/org/eclipse/mylyn/internal/hudson/ui/HudsonDiscovery.java
rm -rf org.eclipse.mylyn.builds/org.eclipse.mylyn.hudson.ui/src/org/eclipse/mylyn/internal/hudson/ui/HudsonUiPlugin.java

# Disable plugins we can live without (they are skipped by default anyway)
for p in findbugs-maven-plugin maven-pmd-plugin jacoco-maven-plugin ; do
  grep -l -r --include="pom.xml" $p . | \
    ( while read pom_path; do %pom_remove_plugin :$p $pom_path ; done ) ;
done

# Disable site modules, we don't need them
for site in $(grep -l -r --include="pom.xml" eclipse-update-site .) ; do
  module=$(basename $(dirname $site)); dir=$(dirname $(dirname $site))
  %pom_disable_module $module $dir
done

# Disable modules we can't build yet
%pom_disable_module org.eclipse.mylyn.subclipse-feature org.eclipse.mylyn.versions
%pom_disable_module org.eclipse.mylyn.subclipse.core org.eclipse.mylyn.versions
%pom_disable_module org.eclipse.mylyn.subclipse.ui org.eclipse.mylyn.versions
%pom_xpath_remove "includes[@id='org.eclipse.mylyn.subclipse']" org.eclipse.mylyn.versions/org.eclipse.mylyn.versions.development-feature/feature.xml
%pom_disable_module org.eclipse.mylyn.reviews .
sed -i -e '/\(gerrit\|reviews\)/d' org.eclipse.mylyn/org.eclipse.mylyn.tests/META-INF/MANIFEST.MF
sed -i -e '/AllGerritTests/d' -e '/AllReviewsTests/d' org.eclipse.mylyn/org.eclipse.mylyn.tests/src/org/eclipse/mylyn/tests/All*Tests.java
%pom_remove_dep ":org.eclipse.mylyn.gerrit.feature.feature.group" org.eclipse.mylyn/org.eclipse.mylyn.tests/pom.xml

# Don't build artifacts that we don't ship
%pom_disable_module org.eclipse.mylyn.commons.tck-feature org.eclipse.mylyn.commons
%pom_disable_module org.eclipse.mylyn.wikitext-standalone org.eclipse.mylyn.docs
%pom_disable_module org.eclipse.mylyn.wikitext.core.maven org.eclipse.mylyn.docs

# These are not intended to be shipped by upstream, see ebz#467669 and ebz#467694
%pom_disable_module org.eclipse.mylyn.commons.identity.ui org.eclipse.mylyn.commons
%pom_disable_module org.eclipse.mylyn.docs.epub.ant.core org.eclipse.mylyn.docs

# Correct bundle names
sed -i -e "s/org.hamcrest;/org.hamcrest.core;/g" `find . -name MANIFEST.MF`
sed -i -e "s/org.mockito;/org.mockito.mockito-core;/g"  `find . -name MANIFEST.MF`
sed -i -e "s/org.apache.ant.source;/org.apache.ant;/g"  `find . -name MANIFEST.MF`

# Use default buildtimestamp source
%pom_remove_dep :tycho-buildtimestamp-jgit org.eclipse.mylyn/org.eclipse.mylyn-parent
%pom_remove_dep :tycho-sourceref-jgit org.eclipse.mylyn/org.eclipse.mylyn-parent
sed -i -e "/<sourceReferences>/,+3d" org.eclipse.mylyn/org.eclipse.mylyn-parent/pom.xml

# Add descriptors to allow tests to run
sed -i -e "s@<addMavenDescriptor>false<@<addMavenDescriptor>true<@" org.eclipse.mylyn/org.eclipse.mylyn-parent/pom.xml

# Integrate incubator bundles
%pom_set_parent org.eclipse.mylyn.tasks:org.eclipse.mylyn.tasks-parent:%{version}-SNAPSHOT org.eclipse.mylyn.tasks/org.eclipse.mylyn.trac.wiki/pom.xml
%pom_set_parent org.eclipse.mylyn.tasks:org.eclipse.mylyn.tasks-parent:%{version}-SNAPSHOT org.eclipse.mylyn.tasks/org.eclipse.mylyn.trac.wiki-feature/pom.xml
%pom_set_parent org.eclipse.mylyn.tasks:org.eclipse.mylyn.tasks-parent:%{version}-SNAPSHOT org.eclipse.mylyn.tasks/org.eclipse.mylyn.web.tasks/pom.xml
%pom_set_parent org.eclipse.mylyn.tasks:org.eclipse.mylyn.tasks-parent:%{version}-SNAPSHOT org.eclipse.mylyn.tasks/org.eclipse.mylyn.web.tasks-feature/pom.xml

rm org.eclipse.mylyn.builds/org.eclipse.mylyn.hudson.ui/src/org/eclipse/mylyn/internal/hudson/ui/HudsonStartup.java

#Be more tolerant for objenesis
sed -i -e "s/1.0.0,2.0.0/1.0.0,3.0.0/g" org.eclipse.mylyn.builds/org.eclipse.mylyn.builds.tests/META-INF/MANIFEST.MF
sed -i -e "s/1.0.0,2.0.0/1.0.0,3.0.0/g" org.eclipse.mylyn.context/org.eclipse.mylyn.context.tests/META-INF/MANIFEST.MF
sed -i -e "s/1.0.0,2.0.0/1.0.0,3.0.0/g" org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.ui.tests/META-INF/MANIFEST.MF
sed -i -e "s/1.0.0,2.0.0/1.0.0,3.0.0/g" org.eclipse.mylyn.tasks/org.eclipse.mylyn.tasks.core.tests/META-INF/MANIFEST.MF
sed -i -e "s/1.0.0,2.0.0/1.0.0,3.0.0/g" org.eclipse.mylyn.tasks/org.eclipse.mylyn.tasks.ui.tests/META-INF/MANIFEST.MF
sed -i -e "s/1.0.0,2.0.0/1.0.0,3.0.0/g" org.eclipse.mylyn.tasks/org.eclipse.mylyn.trac.core.tests/META-INF/MANIFEST.MF
sed -i -e "s/1.0.0,2.0.0/1.0.0,3.0.0/g" org.eclipse.mylyn.tasks/org.eclipse.mylyn.trac.ui.tests/META-INF/MANIFEST.MF
sed -i -e "s/1.0.0,2.0.0/1.0.0,3.0.0/g" org.eclipse.mylyn.docs/org.eclipse.mylyn.wikitext.core.tests/META-INF/MANIFEST.MF
sed -i -e "s/1.0.0,2.0.0/1.0.0,3.0.0/g" org.eclipse.mylyn.docs/org.eclipse.mylyn.wikitext.core.osgi.tests/META-INF/MANIFEST.MF
sed -i -e "s/1.0.0,2.0.0/1.0.0,3.0.0/g" org.eclipse.mylyn.docs/org.eclipse.mylyn.wikitext.html.tests/META-INF/MANIFEST.MF
sed -i -e "s/1.0.0,2.0.0/1.0.0,3.0.0/g" org.eclipse.mylyn.docs/org.eclipse.mylyn.wikitext.commonmark.tests/META-INF/MANIFEST.MF

#Set source level to 1.8 for bundles which require it
sed -i -e "s/JavaSE-1.7/JavaSE-1.8/g" org.eclipse.mylyn.tasks/org.eclipse.mylyn.tasks.core/META-INF/MANIFEST.MF
sed -i -e "s/JavaSE-1.7/JavaSE-1.8/g" org.eclipse.mylyn.tasks/org.eclipse.mylyn.tasks.ui/META-INF/MANIFEST.MF

sed -i -e "s|@NonNull||g" org.eclipse.mylyn.tasks/connector-bugzilla-rest/org.eclipse.mylyn.bugzilla.rest.core/src/org/eclipse/mylyn/internal/bugzilla/rest/core/RepositoryKey.java

%mvn_package "::{target,pom}::" __noinstall
%mvn_package "::jar:sources:" sdk
%mvn_package ":*.sdk{,_feature}" sdk
%mvn_package ":org.eclipse.mylyn.tests.util" sdk
%mvn_package ":org.eclipse.mylyn.{context,commons}.sdk.util" sdk
%mvn_package ":org.eclipse.mylyn.context.sdk.java" sdk
%mvn_package ":org.eclipse.mylyn.*development" sdk
%mvn_package ":*.test{s,_feature}" tests
%mvn_package "org.eclipse.mylyn.builds:*hudson*" builds-hudson
%mvn_package "org.eclipse.mylyn.builds:" builds
%mvn_package "org.eclipse.mylyn.context:*cdt.mylyn*" context-cdt
%mvn_package "org.eclipse.mylyn.context:*mylyn.pde*" context-pde
%mvn_package "org.eclipse.mylyn.context:*{java_feature,java.tasks,java.ui,ide.ant,debug.ui}*" context-java
%mvn_package "org.eclipse.mylyn.docs.epub:" docs-epub
%mvn_package "org.eclipse.mylyn.docs:" docs
%mvn_package "org.eclipse.mylyn.tasks:*bugzilla*" tasks-bugzilla
%mvn_package "org.eclipse.mylyn.tasks:*trac*" tasks-trac
%mvn_package "org.eclipse.mylyn.tasks:*web.tasks*" tasks-web
%mvn_package "org.eclipse.mylyn.versions:*cvs*" versions-cvs
%mvn_package "org.eclipse.mylyn.versions:*git*" versions-git
%mvn_package "org.eclipse.mylyn.versions:" versions
%mvn_package "org.eclipse.mylyn{,.commons,.context,.context.features,.tasks}:" commons

# TODO fix this
for b in org.eclipse.mylyn.docs/org.eclipse.mylyn.wikitext.commonmark.tests ; do
  sed -i "/^Bundle-Localization/d" $b/META-INF/MANIFEST.MF
  sed -i "s|META-INF/l10n/bundle\.properties|OSGI-INF/|" $b/build.properties
  mkdir -p $b/OSGI-INF/l10n
  mv $b/META-INF/l10n/bundle.properties $b/OSGI-INF/l10n/bundle.properties
done
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%mvn_build -f -j -- -Ddist.qualifier="\'v\'yyyyMMdd-HHmm"
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%mvn_install

install %{SOURCE6} \
  %{buildroot}%{_datadir}/eclipse/%{droplets}/mylyn-tasks-bugzilla/eclipse/redhat-bugzilla-custom-transitions.txt
rm %{buildroot}%{_datadir}/eclipse/%{droplets}/mylyn-sdk/eclipse/plugins/org.mockito.mockito-core_*
rm %{buildroot}%{_datadir}/eclipse/%{droplets}/mylyn-sdk/eclipse/plugins/net.sf.cglib.core_*
rm -f %{buildroot}%{_datadir}/eclipse/%{droplets}/mylyn-docs-epub/eclipse/plugins/net.sf.cglib.core_*
sed -i '/org.mockito.mockito-core_/ d' .mfiles-sdk
sed -i '/net.sf.cglib.core_/ d' .mfiles-sdk .mfiles-docs-epub
%{?scl:EOF}


%files -f .mfiles-commons

%files context-java -f .mfiles-context-java

%files context-pde -f .mfiles-context-pde

%files context-cdt -f .mfiles-context-cdt

%files tasks-bugzilla -f .mfiles-tasks-bugzilla
%{_datadir}/eclipse/%{droplets}/mylyn-tasks-bugzilla/eclipse/redhat-bugzilla-custom-transitions.txt

%files tasks-trac -f .mfiles-tasks-trac

%files tasks-web -f .mfiles-tasks-web

%files docs-wikitext -f .mfiles-docs

%files docs-epub -f .mfiles-docs-epub

%files versions -f .mfiles-versions

%files versions-git -f .mfiles-versions-git

%files versions-cvs -f .mfiles-versions-cvs

%files builds -f .mfiles-builds

%files builds-hudson -f .mfiles-builds-hudson

%files sdk -f .mfiles-sdk

%files tests -f .mfiles-tests

%changelog
* Wed Apr 06 2016 Mat Booth <mat.booth@redhat.com> - 3.18.0-5.4
- Fix broken cglib symlink in doc-epub, fixes rhbz#1311007

* Mon Apr 04 2016 Mat Booth <mat.booth@redhat.com> - 3.18.0-5.3
- Patch to fix bugzilla connector tests, rhbz#1263098
- Patch to fix versions tests, rhbz#1315731

* Tue Feb 16 2016 Mat Booth <mat.booth@redhat.com> - 3.18.0-5.2
- Rebuilt to regenerate symlinks to mockito/cglib
- rhbz#1263096, rhbz#1263092

* Fri Feb 12 2016 Mat Booth <mat.booth@redhat.com> - 3.18.0-5.1
- Import latest from Fedora

* Fri Feb 12 2016 Mat Booth <mat.booth@redhat.com> - 3.18.0-5
- Only use lucene 4 on F22

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Roland Grunberg <rgrunber@redhat.com> - 3.18.0-3
- Move org.eclipse.mylyn.*development features into mylyn-sdk.

* Thu Jan 14 2016 Mat Booth <mat.booth@redhat.com> - 3.18.0-2.1
- Import latest from Fedora
- Drop the subclipse package
- Manually remove mockito from sdk, and cglib from doc-epub

* Wed Jan 13 2016 Mat Booth <mat.booth@redhat.com> - 3.18.0-2
- Add missing BR/Rs needed for tests to run
- Include maven descriptors to allow tests to be discovered
- Fixes rhbz#1271125 - no results from mylyn-tests

* Tue Jan 12 2016 Mat Booth <mat.booth@redhat.com> - 3.18.0-1
- Update to latest release

* Mon Jan 11 2016 Roland Grunberg <rgrunber@redhat.com> - 3.17.0-3
- Bump release for rebuild.

* Mon Oct 19 2015 Roland Grunberg <rgrunber@redhat.com> - 3.17.0-2
- Fix Mylyn Task List decorator icons. EBZ #461443
- Fix layout of Task Repository Properties view. EBZ #472409

* Tue Sep 29 2015 Sopot Cela <scela@redhat.com> -3.17.0-1
- Updated to 3.17.0 for Mars.1 release

* Mon Aug 31 2015 Roland Grunberg <rgrunber@redhat.com> - 3.16.0-3
- Minor changes to build as a droplet.

* Tue Jul 28 2015 Roland Grunberg <rgrunber@redhat.com> - 3.16.0-2
- Rebuild for correcting symbolic links to objectweb-asm.

* Thu Jun 25 2015 Alexander Kurtakov <akurtako@redhat.com> 3.16.0-1
- Update to 3.16.0 final release.

* Wed Jun 24 2015 Alexander Kurtakov <akurtako@redhat.com> 3.16.0-0.3.git4d4c9dd
- Fix build with Lucene 5.x.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.0-0.2.git4d4c9dd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Mat Booth <mat.booth@redhat.com> - 3.16.0-0.1.git4d4c9dd
- Update to Mars release candidate

* Thu May 28 2015 Alexander Kurtakov <akurtako@redhat.com> 3.15.0-2
- Fix build against latest jgit.

* Thu May 14 2015 Alexander Kurtakov <akurtako@redhat.com> 3.15.0-1
- Update to upstream 3.15.0.

* Thu Feb 19 2015 Alexander Kurtakov <akurtako@redhat.com> 3.14.2-1
- Update to upstream 3.14.2.

* Thu Feb  5 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.14.0-3
- Rebuild to fix auto-requires

* Thu Jan 29 2015 Mat Booth <mat.booth@redhat.com> - 3.14.0-2
- Build/install with mvn_build/mvn_install, let xmvn auto generate
  requires and provides
- Fold context-team and context-ide into base package, it longer makes
  sense to have these as separate sub packages
- Drop update-site patch
- Add patch to explicitly require hamcrest for tests that need it
- Remove other misc cruft from spec file that is no longer needed

* Mon Jan 12 2015 Alexander Kurtakov <akurtako@redhat.com> 3.14.0-1
- Update to 3.14.

* Thu Nov 13 2014 Alexander Kurtakov <akurtako@redhat.com> 3.13.0-2
- Update lucene4 patch to work properly.

* Thu Oct 02 2014 Mat Booth <mat.booth@redhat.com> - 3.13.0-1
- Update to 3.13.0 release

* Wed Sep 24 2014 Roland Grunberg <rgrunber@redhat.com> - 3.12.0-4
- Disable pack-and-sign/build.xml.

* Fri Aug 15 2014 Mat Booth <mat.booth@redhat.com> - 3.12.0-3
- Ensure the qualifier buildtimestamp is lexigraphically greater than upstream's
- Fix guava being owned by more than one package
- Fix broken symlinks for gson and jsoup

* Tue Jul 22 2014 Sami Wagiaalla <swagiaal@redhat.com> - 3.12.0-2
- Rebuild for new eclipse-pde.

* Thu Jul 10 2014 Sami Wagiaalla <swagiaal@redhat.com> - 3.12.0-1
- Add missing Rs to mylyn-tests

* Thu Jul 10 2014 Sami Wagiaalla <swagiaal@redhat.com> - 3.12.0-0.7
- Update to R_3_12_0 tag.
- Add mylyn-tests package.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.0-0.6.git20140509
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Alexander Kurtakov <akurtako@redhat.com> 3.12.0-0.5.git20140509
- Fix broken requires.

* Wed May 28 2014 Alexander Kurtakov <akurtako@redhat.com> 3.12.0-0.4.git20140509
- Drop old requires.

* Wed May 28 2014 Alexander Kurtakov <akurtako@redhat.com> 3.12.0-0.3.git20140509
- Drop old Provides/Requires.

* Sat May 10 2014 Alexander Kurtakov <akurtako@redhat.com> 3.12.0-0.2.git20140509
- Drop useless BR on javamail.

* Sat May 10 2014 Alexander Kurtakov <akurtako@redhat.com> 3.12.0-0.1.git20140509
- First 3.12.0 pre-release

* Mon Mar 31 2014 Alexander Kurtakov <akurtako@redhat.com> 3.11.0-1
- Update to upstream 3.11.0 release.

* Tue Mar 11 2014 Alexander Kurtakov <akurtako@redhat.com> 3.10.0-4
- Bump release for rebuild.
- Make the lucene range include 4.x.

* Fri Feb 28 2014 Roland Grunberg <rgrunber@redhat.com> - 3.10.0-3
- Change R:java to R:java-headless (Bug 1068050).

* Fri Feb 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.10.0-2
- Fix usage of %%pom_disable_module macro

* Tue Nov 12 2013 Alexander Kurtakov <akurtako@redhat.com> 3.10.0-1
- Update to 3.10.
- Drop compat sources and patches as no longer needed.
- Switch to xz for sources.

* Wed Nov 06 2013 Roland Grunberg <rgrunber@redhat.com> 3.9.1-4
- Include fix for Eclipse bug 419869.

* Fri Oct 11 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.1-3
- Include fix for Eclipse bug 419133. 

* Thu Oct 3 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.1-2
- Add a workaround for a build failing on ARM.

* Thu Oct 3 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.1-1
- Update to Kepler SR1.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.0-2
- Adjust the build for the latest javamail.

* Fri Jun 28 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.0-1
- Use release tagged upstream.

* Tue Jun 18 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.0-0.8.gita6b7cd
- Update to Kepler release.

* Mon Jun 10 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.0-0.7.git2ad84d
- Fix for bug 403024.

* Fri Jun 7 2013 Roland Grunberg <rgrunber@redhat.com> 3.9.0-0.6.git2ad84d
- Update to latest upstream.

* Fri May 31 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.0-0.5.gita6b7cd
- Don't require jacoco for build.
- Update latest to latest upstream.

* Tue May 14 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.0-0.4.git8b0964
- Rebuild to pick up recent dependencies.

* Thu May 2 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.0-0.3.git8b0964
- Update to latest upstream.

* Fri Mar 15 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.0-0.2.gitf9e1cd
- Make noarch always.

* Fri Mar 1 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.0-0.1.gitf9e1cd
- Update to latest upstream.
- Initial SCLization.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.8.2-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Nov 23 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.8.2-2
- Remove javax.xml.

* Tue Oct 2 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.8.2-1
- Update to 3.8.2 upstream release.

* Tue Sep 18 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.8.1-2
- Replace xmlrpc3 with xmlrpc to fix broken dependencies.

* Mon Aug 20 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.8.1-1
- Update to latest upstream release.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 13 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.8.0-5
- Improve obsoletes/conflicts to prevent dissappearing after
  update packages and mixing versions.

* Thu Jul 12 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.8.0-4
- Change the root location of all files.

* Wed Jul 11 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.8.0-3
- Symlink the wsdl jar provided by axis package.

* Tue Jul 10 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.8.0-2
- Add proper BR for jpackage-utils and maven.

* Tue Jul 10 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.8.0-1
- Completely repackaged mylyn.
- Added epub feature.
- Added support for subclipse.

* Mon May 7 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.7.0-5
- Patch for bug 378230 added.

* Mon Apr 30 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.7.0-4
- Include schema description.

* Fri Apr 13 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.7.0-3
- Move to eclipse 4.2.
- Build help.
- Fix the minimum eclipse-rcp requirement

* Mon Apr 2 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.7.0-2
- Bump version to fix upgradepath.

* Mon Mar 26 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.7.0-1
- Update to upstream 3.7.0 release

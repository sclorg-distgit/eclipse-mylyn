%{?scl:%scl_package eclipse-mylyn}
%{!?scl:%global pkg_name %{name}}

%global install_loc         %{_datadir}/eclipse/dropins
%global tag R_3_14_2
%global incubator_tag e963896478edf4fb7b4474895b15c6359aaa9a17

%{!?scl:%global _non_scl_javadir %{_javadir}}
%{?scl:%global _non_scl_javadir /usr/share/java}

%{?java_common_find_provides_and_requires}

Name:    %{?scl_prefix}eclipse-mylyn
Summary: Eclipse Mylyn main feature.
Version: 3.14.2
Release: 1.bootstrap1%{?dist}
License: EPL
URL: http://www.eclipse.org/mylyn

# bash fetch-eclipse-mylyn.sh
Source0: %{pkg_name}-%{tag}-fetched-src.tar.xz
Source1: fetch-eclipse-mylyn.sh
Source6: redhat-bugzilla-custom-transitions.txt

Source7: eclipse-mylyn-%{incubator_tag}-incubator-fetched-src.tar.xz
Source8: fetch-eclipse-mylyn-incubator.sh 

Patch0: %{pkg_name}-remove-hudson-discovery.patch
Patch1: %{pkg_name}-add-apache-xmlrpc.patch
Patch2: %{pkg_name}-ensure-sites-build-after-changes.patch
Patch3: %{pkg_name}-disable-online-tests.patch

Patch4: %{pkg_name}-merge-incubator.patch
Patch5: %{pkg_name}-bug-419133.patch
Patch6: lucene4.patch
Patch8: %{pkg_name}-remove-nullable-annotation.patch
Patch9: %{pkg_name}-disable-subclipse.patch

BuildArch: noarch

BuildRequires: %{?scl_prefix}eclipse-platform >= 1:4.2.0
BuildRequires: %{?scl_prefix}eclipse-pde >= 1:4.2.0
BuildRequires: %{?scl_prefix}eclipse-cdt
BuildRequires: %{?scl_prefix}eclipse-egit
BuildRequires: %{?scl_prefix}eclipse-jgit
BuildRequires: %{?scl_prefix}eclipse-license
BuildRequires: %{?scl_prefix}eclipse-emf
BuildRequires: %{?scl_prefix}tycho >= 0.14.1-5
BuildRequires: %{?scl_prefix}eclipse-egit
BuildRequires: %{?scl_prefix_java_common}lucene
BuildRequires: %{?scl_prefix_java_common}lucene-queryparser
BuildRequires: %{?scl_prefix_java_common}maven-local

BuildRequires: %{?scl_prefix_java_common}apache-commons-lang >= 2.6-6
BuildRequires: %{?scl_prefix_java_common}apache-commons-logging
BuildRequires: %{?scl_prefix_java_common}apache-commons-io >= 2.3
BuildRequires: %{?scl_prefix_java_common}ws-commons-util >= 1.0.1-21
BuildRequires: %{?scl_prefix}xmlrpc-client >= 3.1.3
BuildRequires: %{?scl_prefix}xmlrpc-common >= 3.1.3
BuildRequires: %{?scl_prefix}xmlrpc-server >= 3.1.3
BuildRequires: %{?scl_prefix}rome >= 0.9-9
BuildRequires: %{?scl_prefix_java_common}jakarta-commons-httpclient
BuildRequires: %{?scl_prefix_java_common}httpcomponents-client >= 4.1.3-2
BuildRequires: %{?scl_prefix_java_common}httpcomponents-core >= 4.1.4
BuildRequires: %{?scl_prefix_java_common}google-gson >= 2.0.0
BuildRequires: %{?scl_prefix}guava
BuildRequires: %{?scl_prefix_java_common}xalan-j2
BuildRequires: %{?scl_prefix_java_common}junit
BuildRequires: %{?scl_prefix_java_common}hamcrest
BuildRequires: %{?scl_prefix_java_common}objenesis
BuildRequires: %{?scl_prefix}mockito
BuildRequires: %{?scl_prefix_maven}maven-install-plugin
BuildRequires: %{?scl_prefix_maven}maven-deploy-plugin
BuildRequires: %{?scl_prefix_maven}maven-plugin-build-helper
BuildRequires: %{?scl_prefix}tika
BuildRequires: %{?scl_prefix}tika-parsers-epub
BuildRequires: %{?scl_prefix}jsoup

Requires: %{?scl_prefix}eclipse-platform >= 1:4.2.0
Requires: %{?scl_prefix_java_common}apache-commons-lang >= 2.6-6
Requires: %{?scl_prefix_java_common}apache-commons-logging
Requires: %{?scl_prefix_java_common}apache-commons-io >= 2.3
Requires: %{?scl_prefix_java_common}ws-commons-util >= 1.0.1-21
Requires: %{?scl_prefix}xmlrpc-client  >= 3.1.3
Requires: %{?scl_prefix}xmlrpc-common  >= 3.1.3
Requires: %{?scl_prefix}xmlrpc-server  >= 3.1.3
Requires: %{?scl_prefix}rome >= 0.9-9
Requires: %{?scl_prefix_java_common}xml-commons-apis
Requires: %{?scl_prefix_java_common}jakarta-commons-httpclient
Requires: %{?scl_prefix_java_common}httpcomponents-client >= 4.1.3-2
Requires: %{?scl_prefix_java_common}httpcomponents-core >= 4.1.4
Requires: %{?scl_prefix_java_common}jdom >= 1.1.2-3
Requires: %{?scl_prefix}guava
Requires: %{?scl_prefix_java_common}lucene
Requires: %{?scl_prefix_java_common}lucene-queryparser

%description
Mylyn integrates task support into Eclipse. It supports offline editing
for certain task repositories and monitors work activity to hide
information that is not relevant to the current task.

%package context-java
Summary:  Mylyn Bridge:  Java Development
Requires: %{?scl_prefix}eclipse-jdt
Requires: %{name} = %{version}-%{release}

%description context-java
Mylyn Task-Focused UI extensions for JDT.  Provides focusing of Java
element views and editors.

%package context-pde
Summary:  Mylyn Bridge:  Plug-in Development
Requires: %{?scl_prefix}eclipse-pde
Requires: %{name}-context-java = %{version}-%{release}

%description context-pde
Mylyn Task-Focused UI extensions for PDE, Ant, Team Support and CVS.

%package context-cdt
Summary:  Mylyn Bridge:  C/C++ Development
Requires: %{name} = %{version}-%{release}
Requires: %{?scl_prefix}eclipse-cdt

%description context-cdt
Mylyn Task-Focused UI extensions for CDT.  Provides focusing of C/C++
element views and editors.

%package context-team
Summary:  Mylyn Context Connector: Team Support
Requires: %{name} = %{version}-%{release}

%description context-team
Mylyn Task-Focused UI extensions for Team version control.

%package ide
Summary: Mylyn Context Connector: Eclipse IDE
Requires: %{name} = %{version}-%{release}
Requires: %{name}-context-team = %{version}-%{release}

%description ide
Mylyn Task-Focused UI extensions for the Eclipse IDE. 
Provides focusing of common IDE views and editors.

%package tasks-bugzilla
Summary: Mylyn Tasks Connector: Bugzilla
Requires: %{?scl_prefix}eclipse-platform >= 1:4.2.0
Requires: %{name} = %{version}-%{release}

%description tasks-bugzilla
Provides Task List integration, offline support and rich editing for the
open source Bugzilla bug tracker.

%package docs-wikitext
Summary: Mylyn WikiText
Requires: %{?scl_prefix}eclipse-platform >= 1:3.8.0
Requires: %{name} = %{version}-%{release}
Requires: %{?scl_prefix}jsoup
Provides: %{name}-wikitext = %{version}-%{release}

%description docs-wikitext
Enables parsing and display of lightweight markup (wiki text).

%package docs-htmltext
Summary: Mylyn HtmlText
Requires: %{?scl_prefix}eclipse-platform >= 1:3.8.0

%description docs-htmltext
Enables editing of HTML text.

%package docs-epub
Summary: Mylyn EPub
Requires: %{?scl_prefix}eclipse-platform >= 1:3.8.0
Requires: %{name}-docs-wikitext = %{version}-%{release}
Requires: %{?scl_prefix}tika
Requires: %{?scl_prefix}tika-parsers-epub

%description docs-epub
The EPUB framework in Mylyn Docs offers API to create, manipulate,
read and write EPUB formatted files. 

%package  tasks-trac
Summary: Mylyn Tasks Connector: Trac
Requires: %{?scl_prefix}eclipse-platform >= 1:4.2.0
Requires: %{name} = %{version}-%{release}
Requires: %{?scl_prefix_java_common}google-gson

%description tasks-trac
Provides Task List integration, offline support and rich editing
for the open source Trac issue tracker.

%package  tasks-web
Summary: Mylyn Tasks Connector: Web Templates (Advanced) (Incubation)
Requires: %{?scl_prefix}eclipse-platform >= 1:4.2.0
Requires: %{name} = %{version}-%{release}
Requires: %{?scl_prefix}rome >= 0.9-9
Requires: %{?scl_prefix_java_common}jdom >= 1.1.2-3

%description tasks-web
Provides Task List integration for web-based issue trackers
and templates for example projects.

%package versions
Summary: Eclipse Mylyn Versions
Requires: %{name} = %{version}-%{release}

%description versions
Provides a framework for accessing team providers for Eclipse Mylyn.

%package versions-git
Summary: Mylyn Versions Connector: Git
Requires: %{?scl_prefix}eclipse-platform >= 1:3.8.0
Requires: %{?scl_prefix}eclipse-egit >= 0.10.1
Requires: %{name}-versions = %{version}-%{release}

%description versions-git
Provides Git integration for Eclipse Mylyn.

%package versions-cvs
Summary: Mylyn Versions Connector: CVS
Requires: %{?scl_prefix}eclipse-platform >= 1:3.8.0
Requires: %{name}-versions = %{version}-%{release}

%description versions-cvs
Provides CVS integration for Eclipse Mylyn.

%package builds
Summary: Eclipse Mylyn Builds
Requires: %{name} = %{version}-%{release}
Requires: %{?scl_prefix}eclipse-emf
Requires: %{name}-versions = %{version}-%{release}
Requires: %{?scl_prefix_java_common}xml-commons-apis

%description builds
Provides a common framework to interact with continuous integration
build providers using Eclipse Mylyn.

%package builds-hudson
Summary: Mylyn Builds Connector: Hudson/Jenkins
Requires: %{?scl_prefix}eclipse-platform >= 1:4.2.0-0.6
Requires: %{name} = %{version}-%{release}
Requires: %{?scl_prefix_java_common}google-gson >= 1.6.0
Requires: %{name}-builds = %{version}-%{release}

%description builds-hudson
Support for the open source Hudson and Jenkins continuous integration servers.

%package sdk
Summary: Mylyn SDK
Requires: %{name} = %{version}-%{release}
Requires: %{name}-context-java = %{version}-%{release}
Requires: %{name}-context-pde = %{version}-%{release}
Requires: %{name}-context-cdt = %{version}-%{release}
Requires: %{name}-context-team = %{version}-%{release}
Requires: %{name}-ide = %{version}-%{release}
Requires: %{name}-tasks-bugzilla = %{version}-%{release}
Requires: %{name}-docs-wikitext = %{version}-%{release}
Requires: %{name}-docs-htmltext = %{version}-%{release}
Requires: %{name}-tasks-trac = %{version}-%{release}
Requires: %{name}-versions = %{version}-%{release}
Requires: %{name}-versions-git = %{version}-%{release}
Requires: %{name}-versions-cvs = %{version}-%{release}
Requires: %{name}-builds = %{version}-%{release}
Requires: %{name}-builds-hudson = %{version}-%{release}
Requires: %{?scl_prefix_java_common}xalan-j2
Requires: %{?scl_prefix_java_common}hamcrest
Requires: %{?scl_prefix_java_common}objenesis
Requires: %{?scl_prefix_java_common}junit
Requires: %{?scl_prefix}mockito

%description sdk
Sources for all Mylyn bundles

%package tests
Summary: Mylyn test bundles
Requires: %{?scl_prefix}eclipse-tests
Requires: %{?scl_prefix}eclipse-swtbot
%description tests
All the test bundles for mylyn packages.

%prep
%setup -q -n eclipse-mylyn-%{tag}-fetched-src
tar xaf %{SOURCE7} -C org.eclipse.mylyn.tasks --strip-components=1

%patch0
%patch1
%patch2 -b .sav
%patch3 -b .sav
%patch4 -b .sav
%patch5
pushd org.eclipse.mylyn.tasks
%patch6 -b .sav
popd
%patch8
%patch9

%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl_maven} %{scl} - << "EOF"}
#Disable plugins we can live without and for some reason are redundant (unpackaged or causing build failures).
#There must be empty line after each %%pom_* macro invocation.
grep -l -r --include="pom.xml" findbugs-maven-plugin . | ( while read pom_path; do %pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin $pom_path ; done ) ; 
find . -name feature.xml -exec sed -i -e "s/javax.mail/com.sun.mail.javax.mail/" {} \;
grep -l -r --include="pom.xml" maven-pmd-plugin . | ( while read pom_path; do %pom_remove_plugin org.apache.maven.plugins:maven-pmd-plugin $pom_path ; done ) ; 

#Disable modules we can't build yet
%pom_disable_module org.eclipse.mylyn.reviews .

%pom_disable_module org.eclipse.mylyn.commons.tck-feature org.eclipse.mylyn.commons 

%pom_disable_module org.eclipse.mylyn.tests org.eclipse.mylyn

%pom_disable_module org.eclipse.mylyn.test-feature org.eclipse.mylyn.tasks

#Don't build artifacts that we don't ship
%pom_disable_module org.eclipse.mylyn.wikitext-standalone org.eclipse.mylyn.docs
%pom_disable_module org.eclipse.mylyn.wikitext.core.maven org.eclipse.mylyn.docs

#Disable all tests (except one that was easier to build than patch dependent bundles.
# grep -v org.eclipse.mylyn.doc
#grep -l -r --include="pom.xml" "tests" . | ( while read pom_path; do echo `%pom_xpath_remove "*[local-name() = 'module' and contains(text(),'tests') and not(contains(text(),'tests.'))]" $pom_path` ; done ) ;
# Disable tests for which the required bundles are not included in the update site
%pom_disable_module org.eclipse.mylyn.wikitext.creole.tests org.eclipse.mylyn.docs
%pom_disable_module org.eclipse.mylyn.tasks.activity.tests org.eclipse.mylyn.tasks
%pom_disable_module org.eclipse.mylyn.bugzilla.rest.tests org.eclipse.mylyn.tasks/connector-bugzilla-rest
%pom_disable_module org.eclipse.mylyn.bugzilla.rest.core.tests org.eclipse.mylyn.tasks/connector-bugzilla-rest
%pom_disable_module org.eclipse.mylyn.bugzilla.rest.ui.tests org.eclipse.mylyn.tasks/connector-bugzilla-rest
%pom_disable_module org.eclipse.mylyn.subclipse-feature org.eclipse.mylyn.versions
%pom_disable_module org.eclipse.mylyn.subclipse.core org.eclipse.mylyn.versions
%pom_disable_module org.eclipse.mylyn.subclipse.ui org.eclipse.mylyn.versions

#Correct hamcrest and mockito names
sed -i -e "s/org.hamcrest;/org.hamcrest.core;/g" `find . -name MANIFEST.MF`
sed -i -e "s/org.mockito;/org.mockito.mockito-core;/g"  `find . -name MANIFEST.MF`
sed -i -e "s/org.eclipse.core.runtime.compatibility.auth/org.eclipse.core.runtime.compatibility/g"  `find . -name MANIFEST.MF`
sed -i -e "s/org.apache.ant.source;/org.apache.ant;/g"  `find . -name MANIFEST.MF`
sed -i -e "s/org.apache.xmlrpc/org.apache.xmlrpc,org.apache.xmlrpc.common,org.apache.xmlrpc.server/g" org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.tests/META-INF/MANIFEST.MF
sed -i -e "s/org.apache.xmlrpc;bundle-version=\"3.0.0\"/org.apache.xmlrpc,org.apache.xmlrpc.common/g" org.eclipse.mylyn.tasks/org.eclipse.mylyn.trac.tests/META-INF/MANIFEST.MF

#Remove all architectures that do not match current build architecture.
%pom_xpath_remove "*[local-name() = 'environment' and 
       (child::*[local-name() = 'os' and not(text() = 'linux')] 
            or child::*[local-name() = 'ws' and not(text() = 'gtk')] 
            or child::*[local-name() = 'arch' and not(text() = '%{_arch}')]) ]" org.eclipse.mylyn/org.eclipse.mylyn-parent/pom.xml

#Use default buildtimestamp source
%pom_remove_dep :tycho-buildtimestamp-jgit org.eclipse.mylyn/org.eclipse.mylyn-parent
%pom_remove_dep :tycho-sourceref-jgit org.eclipse.mylyn/org.eclipse.mylyn-parent
sed -i -e "/<sourceReferences>/,+3d" org.eclipse.mylyn/org.eclipse.mylyn-parent/pom.xml

%pom_remove_plugin :jacoco-maven-plugin org.eclipse.mylyn/org.eclipse.mylyn.maven-parent/pom.xml
%pom_remove_plugin :jacoco-maven-plugin org.eclipse.mylyn/org.eclipse.mylyn-parent/pom.xml
%pom_set_parent org.eclipse.mylyn.tasks:org.eclipse.mylyn.tasks-parent:%{version}-SNAPSHOT org.eclipse.mylyn.tasks/org.eclipse.mylyn.trac.wiki/pom.xml
%pom_set_parent org.eclipse.mylyn.tasks:org.eclipse.mylyn.tasks-parent:%{version}-SNAPSHOT org.eclipse.mylyn.tasks/org.eclipse.mylyn.trac.wiki-feature/pom.xml
%pom_set_parent org.eclipse.mylyn.tasks:org.eclipse.mylyn.tasks-parent:%{version}-SNAPSHOT org.eclipse.mylyn.tasks/org.eclipse.mylyn.web.tasks/pom.xml
%pom_set_parent org.eclipse.mylyn.tasks:org.eclipse.mylyn.tasks-parent:%{version}-SNAPSHOT org.eclipse.mylyn.tasks/org.eclipse.mylyn.web.tasks-feature/pom.xml
sed -i -e "s|3.11.0-SNAPSHOT|3.12.0-SNAPSHOT|g" org.eclipse.mylyn.docs/pom.xml

rm org.eclipse.mylyn.builds/org.eclipse.mylyn.hudson.ui/src/org/eclipse/mylyn/internal/hudson/ui/HudsonStartup.java

#Be more tolerant for guava
sed -i -e "s/compatible/greaterOrEqual/g" org.eclipse.mylyn.versions/org.eclipse.mylyn.versions.sdk-feature/feature.xml
sed -i -e "s/e3.5/e3.6/g" org.eclipse.mylyn.commons/org.eclipse.mylyn.commons-target/pom.xml

#Disable pack-and-sign/build.xml
%pom_remove_plugin org.apache.maven.plugins:maven-antrun-plugin org.eclipse.mylyn/org.eclipse.mylyn-site

sed -i -e "s|@NonNull||g" org.eclipse.mylyn.tasks/connector-bugzilla-rest/org.eclipse.mylyn.bugzilla.rest.core/src/org/eclipse/mylyn/internal/bugzilla/rest/core/RepositoryKey.java
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl_maven} %{scl} - << "EOF"}
export MAVEN_OPTS="-XX:CompileCommand=exclude,org/eclipse/tycho/core/osgitools/EquinoxResolver,newState ${MAVEN_OPTS}"
xmvn -o clean verify -Ddist.qualifier="'v'yyyyMMdd-HHmm" -Dmaven.test.skip=true
%{?scl:EOF}

%install
install -d %{buildroot}%{install_loc}/mylyn/eclipse/plugins
install -d %{buildroot}%{install_loc}/mylyn/eclipse/features

cp  org.eclipse.mylyn/org.eclipse.mylyn-site/target/site/plugins/*.jar %{buildroot}%{install_loc}/mylyn/eclipse/plugins/

pushd %{buildroot}%{install_loc}/mylyn/eclipse/plugins/

	rm com.google.gson_*.jar
	ln -s %{_javadir_java_common}/google-gson.jar

	rm com.sun.syndication_*.jar
	ln -s %{_javadir}/rome*.jar

	rm javax.xml_*.jar
	ln -s %{_javadir_java_common}/jaxp.jar

	rm org.apache.xerces_*.jar
	ln -s %{_javadir_java_common}/xerces-j2.jar

	rm org.apache.xml.resolver_*.jar
	ln -s %{_javadir_java_common}/xml-commons-resolver.jar

	rm org.apache.xml.serializer*.jar
	ln -s %{_javadir_java_common}/xalan-j2-serializer.jar

	rm org.apache.commons.io_*.jar
	ln -s %{_javadir_java_common}/apache-commons-io.jar

	rm org.apache.commons.lang_*.jar
	ln -s %{_javadir_java_common}/apache-commons-lang.jar

	rm org.apache.commons.httpclient_*.jar
	ln -s %{_javadir_java_common}/commons-httpclient.jar

	rm org.apache.ws.commons.util_*.jar
	ln -s %{_javadir_java_common}/ws-commons-util.jar
	
	rm org.apache.xmlrpc_*.jar
	ln -s %{_javadir}/xmlrpc-client.jar
	ln -s %{_javadir}/xmlrpc-common.jar
	ln -s %{_javadir}/xmlrpc-server.jar

	rm org.jdom_*.jar
	ln -s %{_javadir_java_common}/jdom.jar

	rm org.jsoup_*.jar
	ln -s %{_javadir}/jsoup/jsoup.jar

	rm com.google.guava_*.jar
	ln -s %{_javadir}/guava.jar

    rm org.apache.tika.core_*.jar
	ln -s %{_javadir}/tika/tika-core.jar

    rm org.apache.tika.parsers_*.jar
	ln -s %{_javadir}/tika/tika-parsers.jar

	rm org.apache.lucene.core_*.jar #bundled by platform
	rm org.apache.httpcomponents.httpclient_*.jar #bundled by platform
	rm org.apache.httpcomponents.httpcore_*.jar #bundled by platform
	rm org.apache.commons.logging_*.jar #bundled by platform
	rm org.apache.commons.codec_*.jar #bundled by platform
popd

mkdir -p %{buildroot}%{install_loc}/mylyn/eclipse/features
for f in `ls -1 org.eclipse.mylyn/org.eclipse.mylyn-site/target/site/features/ | grep jar$`; do
    unzip org.eclipse.mylyn/org.eclipse.mylyn-site/target/site/features/$f -d %{buildroot}%{install_loc}/mylyn/eclipse/features/${f/.jar//};
done

install %{SOURCE6} %{buildroot}%{install_loc}/mylyn/eclipse/redhat-bugzilla-custom-transitions.txt

# Collect and install test jars
mkdir -p %{buildroot}%{_javadir}/mylyn-tests/plugins 
set +e
for pom in `find . -name pom.xml`; do
 grep -q '<packaging>eclipse-test-plugin</packaging>' ${pom}
 if [ $? -eq 0 ]; then
   ls ${pom/pom.xml/}'target/'
   testjar=`ls ${pom/pom.xml/}'target/'*.jar | grep -v sources`
   mv ${testjar} %{buildroot}%{_javadir}/mylyn-tests/plugins
 fi
done
set -e

%files
%dir %{install_loc}/mylyn
%dir %{install_loc}/mylyn/eclipse
%dir %{install_loc}/mylyn/eclipse/features/
%dir %{install_loc}/mylyn/eclipse/plugins/
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn_feature_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.tasks.ide_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.tasks.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.tasks.index.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.tasks.index.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.tasks.search_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.tasks.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.tasks.bugs_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.help.ui_*.jar
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.commons_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.commons.activity_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.commons.identity_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.commons.notifications_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories.http_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.discovery_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.monitor_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.activity.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.identity.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.notifications.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.notifications.feed_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.notifications.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.repositories.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.repositories.http.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.repositories.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.screenshots_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.workbench_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.discovery.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.discovery.ui*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.monitor.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.monitor.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.sdk.util_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.xmlrpc_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.net_*.jar
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.context_feature_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.context.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.context.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.resources.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.context.tasks.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/apache-commons-lang.jar
%{install_loc}/mylyn/eclipse/plugins/apache-commons-io.jar
%{install_loc}/mylyn/eclipse/plugins/jdom.jar
%{install_loc}/mylyn/eclipse/plugins/rome*.jar
%{install_loc}/mylyn/eclipse/plugins/xmlrpc-client.jar
%{install_loc}/mylyn/eclipse/plugins/xmlrpc-common.jar
%{install_loc}/mylyn/eclipse/plugins/xmlrpc-server.jar
%{install_loc}/mylyn/eclipse/plugins/commons-httpclient.jar
%{install_loc}/mylyn/eclipse/plugins/ws-commons-util.jar
%{install_loc}/mylyn/eclipse/plugins/jaxp.jar
%{install_loc}/mylyn/eclipse/plugins/google-gson.jar
%{install_loc}/mylyn/eclipse/plugins/guava.jar

%files context-java
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.java_feature_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.java.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.java.tasks_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.ide.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.ide.ant_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.debug.ui_*.jar

%files context-pde
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.pde_feature_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.pde.ui_*.jar

%files context-cdt
%{install_loc}/mylyn/eclipse/features/org.eclipse.cdt.mylyn_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.cdt.mylyn.ui_*.jar

%files context-team
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.team_feature_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.team.ui_*.jar

%files ide
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.ide_feature_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.team.cvs_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.bugzilla.ide_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.ide.ui_*.jar

%files tasks-bugzilla
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.bugzilla_feature_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.bugzilla.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.bugzilla.ui_*.jar
%{install_loc}/mylyn/eclipse/redhat-bugzilla-custom-transitions.txt

%files tasks-trac
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.trac_feature_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.trac.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.trac.ui_*.jar
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.trac.wiki_feature_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.trac.wiki_*.jar

%files tasks-web
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.web.tasks_feature_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.web.tasks_*.jar

%files docs-wikitext
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.wikitext_feature_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.core.ant_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.core.osgi_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.textile.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.html.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.mediawiki.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.mediawiki.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.markdown.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.markdown.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.confluence.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.tracwiki.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.twiki.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.help.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.textile.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.confluence.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.tracwiki.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.twiki.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.tasks.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.context.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/jsoup.jar

%files docs-htmltext
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.htmltext_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.htmltext.ui_*.jar

%files docs-epub
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.docs.epub_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.docs.epub.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.docs.epub.help_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.docs.epub.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.docs.epub.ant.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/tika*.jar

%files versions
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.versions_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.versions.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.versions.ui_*.jar

%files versions-git
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.git_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.git.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.git.ui_*.jar

%files versions-cvs
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.cvs_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.cvs.core_*.jar

%files builds
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.builds_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.builds.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.builds.ui_*.jar

%files builds-hudson
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.hudson_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.hudson.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.hudson.ui_*.jar

%files sdk
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.builds.sdk_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.context.sdk_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.commons.sdk_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.docs.epub.sdk_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.docs.sdk_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.sdk_feature_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.versions.sdk_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.wikitext.sdk_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.context.sdk.java_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.context.sdk.util_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.help.sdk_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.tests.util_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.*.source_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.cdt.mylyn.ui.source_*.jar
%{install_loc}/mylyn/eclipse/plugins/xerces-j2.jar
%{install_loc}/mylyn/eclipse/plugins/xalan-j2-serializer.jar
%{install_loc}/mylyn/eclipse/plugins/xml-commons-resolver.jar

%files tests
%{_javadir}/mylyn-tests

%changelog
* Mon Feb 23 2015 Roland Grunberg <rgrunber@redhat.com> - 3.14.2-1
- Update to 3.14.2.
- Resolves: rhbz#1175108.

* Sun Jan 25 2015 Mat Booth <mat.booth@redhat.com> - 3.14.0-6
- Resolves: rhbz#1185541, rhbz#1185542
- Add missing requires on tika/wikitext to docs-epub subpackage

* Fri Jan 16 2015 Roland Grunberg <rgrunber@redhat.com> - 3.14.0-5
- Remove unnecessary patch.

* Fri Jan 16 2015 Roland Grunberg <rgrunber@redhat.com> - 3.14.0-4
- Add proper Requires to resolve broken symlinks.

* Thu Jan 15 2015 Roland Grunberg <rgrunber@redhat.com> - 3.14.0-3
- Fix broken symlinks.

* Thu Jan 15 2015 Roland Grunberg <rgrunber@redhat.com> - 3.14.0-2
- SCL-ize.
- Adapt lucene4.patch to support 4.8 instead of 4.10.
- Relax support of only Java 8.
- Disable support for Subclipse.

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

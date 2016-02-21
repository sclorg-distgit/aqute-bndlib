%global pkg_name aqute-bndlib
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}


Name:           %{?scl_prefix}%{pkg_name}
Version:        1.50.0
Release:        8.10%{?dist}
Summary:        BND Library
License:        ASL 2.0
URL:            http://www.aQute.biz/Code/Bnd

Source0:        http://repo1.maven.org/maven2/biz/aQute/bndlib/1.50.0/bndlib-1.50.0.jar
Source1:        http://repo1.maven.org/maven2/biz/aQute/bndlib/1.50.0/bndlib-1.50.0.pom

BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}javapackages-tools
BuildRequires:  %{?scl_prefix_java_common}maven-local

%description
The bnd tool helps you create and diagnose OSGi R4 bundles.
The key functions are:
- Show the manifest and JAR contents of a bundle
- Wrap a JAR so that it becomes a bundle
- Create a Bundle from a specification and a class path
- Verify the validity of the manifest entries
The tool is capable of acting as:
- Command line tool
- File format
- Directives
- Use of macros

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -c -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x

# fixing incomplete source directory structure
mkdir -p src/main/java target/classes
mv -f OSGI-OPT/src/* src/main/java/

# removing bundled classess & junk
rm -rf OSGI-OPT
rm -rf META-INF
rm -rf src/main/java/aQute/bnd/test
find . -iname '*.class' -delete
find . -iname 'packageinfo' -delete

# recycling all data files
mv -f aQute target/classes
mv -f org target/classes

# for building with maven
cp %{SOURCE1} pom.xml

# CR+LF -> LF
sed -i "s|\r||g" LICENSE

%mvn_file : %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
export LC_ALL=en_US.UTF-8
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 1.50.0-8.10
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.50.0-8.9
- maven33 rebuild

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.50.0-8.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.50.0-8.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.50.0-8.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.50.0-8.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.50.0-8.4
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.50.0-8.3
- Remove requires on java

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.50.0-8.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.50.0-8.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.50.0-8
- Mass rebuild 2013-12-27

* Tue Aug 27 2013 Michal Srb <msrb@redhat.com> - 1.50.0-7
- Migrate away from mvn-rpmbuild (Resolves: #997449)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.50.0-6
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.50.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.50.0-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.50.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.50.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Jaromir Capik <jcapik@redhat.com> - 1.50.0-1
- Update to 1.50.0

* Fri Dec 02 2011 Jaromir Capik <jcapik@redhat.com> - 1.43.0-2
- Missing non-class files added

* Thu Sep 15 2011 Jaromir Capik <jcapik@redhat.com> - 1.43.0-1
- Update to 1.43.0
- Spec file changes according to the latest guidelines

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.0.363-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 9 2010 Alexander Kurtakov <akurtako@redhat.com> 0:0.0.363-3
- BR java-devel >= 1.6.0.

* Tue Nov 9 2010 Alexander Kurtakov <akurtako@redhat.com> 0:0.0.363-2
- Fix FTBFS.

* Thu Sep 3 2009 Alexander Kurtakov <akurtako@redhat.com> 0:0.0.363-1
- Update to 0.0.363.

* Wed Aug 19 2009 Andrew Overholt <overholt@redhat.com> 0:0.0.203-4.3
- Add LICENSE
- Clean up Group tag

* Mon Aug 17 2009 Andrew Overholt <overholt@redhat.com> 0:0.0.203-4.2
- Remove gcj support

* Wed May 20 2009 Fernando Nasser <fnasser@redhat.com> 0:0.0.203-4.1
- Remove unedded BRs at Andrew Overholt's recommendation
- Changed libdir to /usr/lib* at 'ajax' suggestion on irc to avoid
  noarch on 64-bit arches problem

* Fri Mar 20 2009 Yong Yang <yyang@redhat.com> 0.0.203-4
- rebuild with new maven2 2.0.8 built in bootstrap mode
- merge from JPP-6

* Tue Jan 15 2009 David Walluck <dwalluck@redhat.com> 0:0.0.203-3
- fix build

* Thu Jan 15 2009 Yong Yang <yyang@redhat.com> 0.0.203-3jpp.1
- Imported from dbhole's maven 2.0.8 packages, initial building

* Tue Mar 11 2008 Deepak Bhole <dbhole@redhat.com> 0.0.203-2jpp.1
- Import from JPackage + change per Fedora requirements

* Thu Feb 14 2008 Ralph Apel <r.apel@r-apel.de> - 0:0.0.203-2jpp
- Add several non class files to jar

* Mon Jan 07 2008 Ralph Apel <r.apel@r-apel.de> - 0:0.0.203-1jpp
- First release

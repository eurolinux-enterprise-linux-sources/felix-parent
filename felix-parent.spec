Name:           felix-parent
Version:        1.2.1
Release:        15%{?dist}
Summary:        Parent POM file for Apache Felix Specs

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://felix.apache.org/
#svn export http://svn.apache.org/repos/asf/felix/releases/felix-parent-1.2.1/
#tar -jcf felix-parent-1.2.1.tar.bz2 felix-parent-1.2.1/
Source0:        %{name}-%{version}.tar.bz2
#Remove mockito-all dependency which is not in koji
Patch0:        %{name}-%{version}-pom.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: junit
BuildRequires: maven-local
BuildRequires: easymock2
BuildRequires: maven-plugin-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-assembly-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-deploy-plugin
BuildRequires: maven-gpg-plugin
BuildRequires: maven-project-info-reports-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-report-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-jxr

Requires: junit
Requires: easymock2
Requires: maven
Requires: maven-plugin-plugin
Requires: maven-compiler-plugin
Requires: maven-install-plugin
Requires: maven-jar-plugin
Requires: maven-javadoc-plugin
Requires: maven-resources-plugin
Requires: maven-assembly-plugin
Requires: maven-source-plugin
Requires: maven-deploy-plugin
Requires: maven-gpg-plugin
Requires: maven-project-info-reports-plugin
Requires: maven-release-plugin
Requires: maven-surefire-plugin
Requires: maven-surefire-report-plugin
Requires: maven-plugin-build-helper
Requires: maven-plugin-jxr

Requires:       jpackage-utils


%description
Parent POM file for Apache Felix Specs.

%prep
%setup -q 
%patch0 -p0 -b .sav
%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin

# legacy depmap (some upstream packages haven't caught up with the
# "felix" -> "felix-parent" rename yet)
%mvn_alias : :felix

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE


%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2.1-15
- Mass rebuild 2013-12-27

* Tue Jul 16 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-14
- Fix Maven alias

* Mon Jul 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-13
- Remove unneeded depmap file

* Mon Jul 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-12
- Update to current packaging guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2.1-10
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Dec 18 2012 Michal Srb <msrb@redhat.com> - 1.2.1-9
- Removed dependency on maven-site-plugin

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 30 2011 Alexander Kurtakov <akurtako@redhat.com> 1.2.1-6
- Fix faulty compiler plugin settings setting source but not target.

* Sun Mar 13 2011 Mat Booth <fedora@matbooth.co.uk> 1.2.1-5
- Add dep on maven-plugin-jxr.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 27 2010 Mat Booth <fedora@matbooth.co.uk> - 1.2.1-3
- Add legacy depmap from maven2-common-poms for felix packages that still
  specify "felix" instead of "felix-parent"

* Tue Jul 20 2010 Hui Wang <huwang@redhat.com> - 1.2.1-2
- Update summary and description
- Add comment in mvn-jpp

* Fri Jul 16 2010 Hui Wang <huwang@redhat.com> - 1.2.1-1
- Initial version of the package

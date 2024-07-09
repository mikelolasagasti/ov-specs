# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/jwalton/gchalk
%global goipath         github.com/jwalton/gchalk
Version:                1.3.0

%gometa -L -f

%global common_description %{expand:
Terminal string styling for go.}

%global golicenses      LICENSE LICENSE-chalk pkg/ansistyles/LICENSE-ansistyles\\\
                        pkg/ansistyles/LICENSE-ansi-styles
%global godocs          README.md architecture.md pkg/ansistyles/README-ansistyles.md

Name:           golang-github-jwalton-gchalk
Release:        %autorelease
Summary:        Terminal string styling for go

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

mv pkg/ansistyles/LICENSE pkg/ansistyles/LICENSE-ansistyles
mv pkg/ansistyles/README.md pkg/ansistyles/README-ansistyles.md

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%install
%gopkginstall

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%gopkgfiles

%changelog
%autochangelog

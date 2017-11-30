Name:           ros-kinetic-control-toolbox
Version:        1.16.0
Release:        0%{?dist}
Summary:        ROS control_toolbox package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/control_toolbox
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-cmake-modules
Requires:       ros-kinetic-control-msgs
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-realtime-tools
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-std-msgs
Requires:       tinyxml-devel
BuildRequires:  ros-kinetic-catkin >= 0.5.68
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-control-msgs
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-realtime-tools
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  tinyxml-devel

%description
The control toolbox contains modules that are useful across all controllers.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Nov 30 2017 Sachin Chitta <sachinc@willowgarage.com> - 1.16.0-0
- Autogenerated by Bloom

* Tue Jun 28 2016 Sachin Chitta <sachinc@willowgarage.com> - 1.15.0-0
- Autogenerated by Bloom

* Tue May 03 2016 Sachin Chitta <sachinc@willowgarage.com> - 1.14.0-0
- Autogenerated by Bloom

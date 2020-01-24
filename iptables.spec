#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xAB4655A126D292E4 (coreteam@netfilter.org)
#
Name     : iptables
Version  : 1.8.4
Release  : 36
URL      : https://www.netfilter.org/projects/iptables/files/iptables-1.8.4.tar.bz2
Source0  : https://www.netfilter.org/projects/iptables/files/iptables-1.8.4.tar.bz2
Source1  : ip6tables-restore.service
Source2  : ip6tables-save.service
Source3  : iptables-restore.service
Source4  : iptables-save.service
Source5  : https://www.netfilter.org/projects/iptables/files/iptables-1.8.4.tar.bz2.sig
Summary  : Shared Xtables code for extensions and iproute2
Group    : Development/Tools
License  : GPL-2.0
Requires: iptables-bin = %{version}-%{release}
Requires: iptables-data = %{version}-%{release}
Requires: iptables-lib = %{version}-%{release}
Requires: iptables-license = %{version}-%{release}
Requires: iptables-man = %{version}-%{release}
Requires: iptables-services = %{version}-%{release}
BuildRequires : bison
BuildRequires : flex
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32libmnl)
BuildRequires : pkgconfig(32libnetfilter_conntrack)
BuildRequires : pkgconfig(32libnfnetlink)
BuildRequires : pkgconfig(32libnftnl)
BuildRequires : pkgconfig(libmnl)
BuildRequires : pkgconfig(libnetfilter_conntrack)
BuildRequires : pkgconfig(libnfnetlink)
BuildRequires : pkgconfig(libnftnl)
Patch1: cve-2012-2663.patch

%description
No detailed description available

%package bin
Summary: bin components for the iptables package.
Group: Binaries
Requires: iptables-data = %{version}-%{release}
Requires: iptables-license = %{version}-%{release}
Requires: iptables-services = %{version}-%{release}

%description bin
bin components for the iptables package.


%package data
Summary: data components for the iptables package.
Group: Data

%description data
data components for the iptables package.


%package dev
Summary: dev components for the iptables package.
Group: Development
Requires: iptables-lib = %{version}-%{release}
Requires: iptables-bin = %{version}-%{release}
Requires: iptables-data = %{version}-%{release}
Provides: iptables-devel = %{version}-%{release}
Requires: iptables = %{version}-%{release}

%description dev
dev components for the iptables package.


%package dev32
Summary: dev32 components for the iptables package.
Group: Default
Requires: iptables-lib32 = %{version}-%{release}
Requires: iptables-bin = %{version}-%{release}
Requires: iptables-data = %{version}-%{release}
Requires: iptables-dev = %{version}-%{release}

%description dev32
dev32 components for the iptables package.


%package extras
Summary: extras components for the iptables package.
Group: Default

%description extras
extras components for the iptables package.


%package lib
Summary: lib components for the iptables package.
Group: Libraries
Requires: iptables-data = %{version}-%{release}
Requires: iptables-license = %{version}-%{release}

%description lib
lib components for the iptables package.


%package lib32
Summary: lib32 components for the iptables package.
Group: Default
Requires: iptables-data = %{version}-%{release}
Requires: iptables-license = %{version}-%{release}

%description lib32
lib32 components for the iptables package.


%package license
Summary: license components for the iptables package.
Group: Default

%description license
license components for the iptables package.


%package man
Summary: man components for the iptables package.
Group: Default

%description man
man components for the iptables package.


%package services
Summary: services components for the iptables package.
Group: Systemd services

%description services
services components for the iptables package.


%prep
%setup -q -n iptables-1.8.4
cd %{_builddir}/iptables-1.8.4
%patch1 -p1
pushd ..
cp -a iptables-1.8.4 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579825955
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --enable-devel --enable-ipv6
make

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --enable-devel --enable-ipv6   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make
popd
%install
export SOURCE_DATE_EPOCH=1579825955
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/iptables
cp %{_builddir}/iptables-1.8.4/COPYING %{buildroot}/usr/share/package-licenses/iptables/4cc77b90af91e615a64ae04893fdffa7939db84c
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/ip6tables-restore.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/ip6tables-save.service
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/iptables-restore.service
install -m 0644 %{SOURCE4} %{buildroot}/usr/lib/systemd/system/iptables-save.service
## Remove excluded files
rm -f %{buildroot}/usr/lib32/xtables/libarpt_mangle.so
rm -f %{buildroot}/usr/lib32/xtables/libebt_802_3.so
rm -f %{buildroot}/usr/lib32/xtables/libebt_ip.so
rm -f %{buildroot}/usr/lib32/xtables/libebt_limit.so
rm -f %{buildroot}/usr/lib32/xtables/libebt_log.so
rm -f %{buildroot}/usr/lib32/xtables/libebt_mark.so
rm -f %{buildroot}/usr/lib32/xtables/libebt_mark_m.so
rm -f %{buildroot}/usr/lib32/xtables/libebt_nflog.so
rm -f %{buildroot}/usr/lib32/xtables/libip6t_DNAT.so
rm -f %{buildroot}/usr/lib32/xtables/libip6t_DNPT.so
rm -f %{buildroot}/usr/lib32/xtables/libip6t_HL.so
rm -f %{buildroot}/usr/lib32/xtables/libip6t_LOG.so
rm -f %{buildroot}/usr/lib32/xtables/libip6t_MASQUERADE.so
rm -f %{buildroot}/usr/lib32/xtables/libip6t_NETMAP.so
rm -f %{buildroot}/usr/lib32/xtables/libip6t_REDIRECT.so
rm -f %{buildroot}/usr/lib32/xtables/libip6t_REJECT.so
rm -f %{buildroot}/usr/lib32/xtables/libip6t_SNAT.so
rm -f %{buildroot}/usr/lib32/xtables/libip6t_SNPT.so
rm -f %{buildroot}/usr/lib32/xtables/libip6t_ah.so
rm -f %{buildroot}/usr/lib32/xtables/libip6t_dst.so
rm -f %{buildroot}/usr/lib32/xtables/libip6t_eui64.so
rm -f %{buildroot}/usr/lib32/xtables/libip6t_frag.so
rm -f %{buildroot}/usr/lib32/xtables/libip6t_hbh.so
rm -f %{buildroot}/usr/lib32/xtables/libip6t_hl.so
rm -f %{buildroot}/usr/lib32/xtables/libip6t_icmp6.so
rm -f %{buildroot}/usr/lib32/xtables/libip6t_ipv6header.so
rm -f %{buildroot}/usr/lib32/xtables/libip6t_mh.so
rm -f %{buildroot}/usr/lib32/xtables/libip6t_rt.so
rm -f %{buildroot}/usr/lib32/xtables/libipt_CLUSTERIP.so
rm -f %{buildroot}/usr/lib32/xtables/libipt_DNAT.so
rm -f %{buildroot}/usr/lib32/xtables/libipt_ECN.so
rm -f %{buildroot}/usr/lib32/xtables/libipt_LOG.so
rm -f %{buildroot}/usr/lib32/xtables/libipt_MASQUERADE.so
rm -f %{buildroot}/usr/lib32/xtables/libipt_NETMAP.so
rm -f %{buildroot}/usr/lib32/xtables/libipt_REDIRECT.so
rm -f %{buildroot}/usr/lib32/xtables/libipt_REJECT.so
rm -f %{buildroot}/usr/lib32/xtables/libipt_SNAT.so
rm -f %{buildroot}/usr/lib32/xtables/libipt_TTL.so
rm -f %{buildroot}/usr/lib32/xtables/libipt_ULOG.so
rm -f %{buildroot}/usr/lib32/xtables/libipt_ah.so
rm -f %{buildroot}/usr/lib32/xtables/libipt_icmp.so
rm -f %{buildroot}/usr/lib32/xtables/libipt_realm.so
rm -f %{buildroot}/usr/lib32/xtables/libipt_ttl.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_AUDIT.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_CHECKSUM.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_CLASSIFY.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_CONNMARK.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_CONNSECMARK.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_CT.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_DSCP.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_HMARK.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_IDLETIMER.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_LED.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_MARK.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_NFLOG.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_NFQUEUE.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_NOTRACK.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_RATEEST.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_SECMARK.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_SET.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_SYNPROXY.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_TCPMSS.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_TCPOPTSTRIP.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_TEE.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_TOS.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_TPROXY.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_TRACE.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_addrtype.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_bpf.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_cgroup.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_cluster.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_comment.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_connbytes.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_connlabel.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_connlimit.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_connmark.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_conntrack.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_cpu.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_dccp.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_devgroup.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_dscp.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_ecn.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_esp.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_hashlimit.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_helper.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_ipcomp.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_iprange.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_ipvs.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_length.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_limit.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_mac.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_mangle.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_mark.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_multiport.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_nfacct.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_osf.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_owner.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_physdev.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_pkttype.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_policy.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_quota.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_rateest.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_recent.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_rpfilter.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_sctp.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_set.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_socket.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_standard.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_state.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_statistic.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_string.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_tcp.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_tcpmss.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_time.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_tos.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_u32.so
rm -f %{buildroot}/usr/lib32/xtables/libxt_udp.so

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/arptables
/usr/bin/arptables-nft
/usr/bin/arptables-nft-restore
/usr/bin/arptables-nft-save
/usr/bin/arptables-restore
/usr/bin/arptables-save
/usr/bin/ebtables
/usr/bin/ebtables-nft
/usr/bin/ebtables-nft-restore
/usr/bin/ebtables-nft-save
/usr/bin/ebtables-restore
/usr/bin/ebtables-save
/usr/bin/ip6tables
/usr/bin/ip6tables-legacy
/usr/bin/ip6tables-legacy-restore
/usr/bin/ip6tables-legacy-save
/usr/bin/ip6tables-nft
/usr/bin/ip6tables-nft-restore
/usr/bin/ip6tables-nft-save
/usr/bin/ip6tables-restore
/usr/bin/ip6tables-restore-translate
/usr/bin/ip6tables-save
/usr/bin/ip6tables-translate
/usr/bin/iptables
/usr/bin/iptables-legacy
/usr/bin/iptables-legacy-restore
/usr/bin/iptables-legacy-save
/usr/bin/iptables-nft
/usr/bin/iptables-nft-restore
/usr/bin/iptables-nft-save
/usr/bin/iptables-restore
/usr/bin/iptables-restore-translate
/usr/bin/iptables-save
/usr/bin/iptables-translate
/usr/bin/iptables-xml
/usr/bin/nfnl_osf
/usr/bin/xtables-legacy-multi
/usr/bin/xtables-monitor
/usr/bin/xtables-nft-multi

%files data
%defattr(-,root,root,-)
/usr/share/xtables/pf.os

%files dev
%defattr(-,root,root,-)
/usr/include/libiptc/ipt_kernel_headers.h
/usr/include/libiptc/libip6tc.h
/usr/include/libiptc/libiptc.h
/usr/include/libiptc/libxtc.h
/usr/include/libiptc/xtcshared.h
/usr/include/xtables-version.h
/usr/include/xtables.h
/usr/lib64/libip4tc.so
/usr/lib64/libip6tc.so
/usr/lib64/libxtables.so
/usr/lib64/pkgconfig/libip4tc.pc
/usr/lib64/pkgconfig/libip6tc.pc
/usr/lib64/pkgconfig/libiptc.pc
/usr/lib64/pkgconfig/xtables.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libip4tc.so
/usr/lib32/libip6tc.so
/usr/lib32/libxtables.so
/usr/lib32/pkgconfig/32libip4tc.pc
/usr/lib32/pkgconfig/32libip6tc.pc
/usr/lib32/pkgconfig/32libiptc.pc
/usr/lib32/pkgconfig/32xtables.pc
/usr/lib32/pkgconfig/libip4tc.pc
/usr/lib32/pkgconfig/libip6tc.pc
/usr/lib32/pkgconfig/libiptc.pc
/usr/lib32/pkgconfig/xtables.pc

%files extras
%defattr(-,root,root,-)
/usr/lib64/libip4tc.so.2
/usr/lib64/libip4tc.so.2.0.0
/usr/lib64/libip6tc.so.2
/usr/lib64/libip6tc.so.2.0.0

%files lib
%defattr(-,root,root,-)
/usr/lib64/libxtables.so.12
/usr/lib64/libxtables.so.12.2.0
/usr/lib64/xtables/libarpt_mangle.so
/usr/lib64/xtables/libebt_802_3.so
/usr/lib64/xtables/libebt_among.so
/usr/lib64/xtables/libebt_arp.so
/usr/lib64/xtables/libebt_arpreply.so
/usr/lib64/xtables/libebt_dnat.so
/usr/lib64/xtables/libebt_ip.so
/usr/lib64/xtables/libebt_ip6.so
/usr/lib64/xtables/libebt_log.so
/usr/lib64/xtables/libebt_mark.so
/usr/lib64/xtables/libebt_mark_m.so
/usr/lib64/xtables/libebt_nflog.so
/usr/lib64/xtables/libebt_pkttype.so
/usr/lib64/xtables/libebt_redirect.so
/usr/lib64/xtables/libebt_snat.so
/usr/lib64/xtables/libebt_stp.so
/usr/lib64/xtables/libebt_vlan.so
/usr/lib64/xtables/libip6t_DNAT.so
/usr/lib64/xtables/libip6t_DNPT.so
/usr/lib64/xtables/libip6t_HL.so
/usr/lib64/xtables/libip6t_LOG.so
/usr/lib64/xtables/libip6t_MASQUERADE.so
/usr/lib64/xtables/libip6t_NETMAP.so
/usr/lib64/xtables/libip6t_REDIRECT.so
/usr/lib64/xtables/libip6t_REJECT.so
/usr/lib64/xtables/libip6t_SNAT.so
/usr/lib64/xtables/libip6t_SNPT.so
/usr/lib64/xtables/libip6t_ah.so
/usr/lib64/xtables/libip6t_dst.so
/usr/lib64/xtables/libip6t_eui64.so
/usr/lib64/xtables/libip6t_frag.so
/usr/lib64/xtables/libip6t_hbh.so
/usr/lib64/xtables/libip6t_hl.so
/usr/lib64/xtables/libip6t_icmp6.so
/usr/lib64/xtables/libip6t_ipv6header.so
/usr/lib64/xtables/libip6t_mh.so
/usr/lib64/xtables/libip6t_rt.so
/usr/lib64/xtables/libip6t_srh.so
/usr/lib64/xtables/libipt_CLUSTERIP.so
/usr/lib64/xtables/libipt_DNAT.so
/usr/lib64/xtables/libipt_ECN.so
/usr/lib64/xtables/libipt_LOG.so
/usr/lib64/xtables/libipt_MASQUERADE.so
/usr/lib64/xtables/libipt_NETMAP.so
/usr/lib64/xtables/libipt_REDIRECT.so
/usr/lib64/xtables/libipt_REJECT.so
/usr/lib64/xtables/libipt_SNAT.so
/usr/lib64/xtables/libipt_TTL.so
/usr/lib64/xtables/libipt_ULOG.so
/usr/lib64/xtables/libipt_ah.so
/usr/lib64/xtables/libipt_icmp.so
/usr/lib64/xtables/libipt_realm.so
/usr/lib64/xtables/libipt_ttl.so
/usr/lib64/xtables/libxt_AUDIT.so
/usr/lib64/xtables/libxt_CHECKSUM.so
/usr/lib64/xtables/libxt_CLASSIFY.so
/usr/lib64/xtables/libxt_CONNMARK.so
/usr/lib64/xtables/libxt_CONNSECMARK.so
/usr/lib64/xtables/libxt_CT.so
/usr/lib64/xtables/libxt_DSCP.so
/usr/lib64/xtables/libxt_HMARK.so
/usr/lib64/xtables/libxt_IDLETIMER.so
/usr/lib64/xtables/libxt_LED.so
/usr/lib64/xtables/libxt_MARK.so
/usr/lib64/xtables/libxt_NFLOG.so
/usr/lib64/xtables/libxt_NFQUEUE.so
/usr/lib64/xtables/libxt_NOTRACK.so
/usr/lib64/xtables/libxt_RATEEST.so
/usr/lib64/xtables/libxt_SECMARK.so
/usr/lib64/xtables/libxt_SET.so
/usr/lib64/xtables/libxt_SYNPROXY.so
/usr/lib64/xtables/libxt_TCPMSS.so
/usr/lib64/xtables/libxt_TCPOPTSTRIP.so
/usr/lib64/xtables/libxt_TEE.so
/usr/lib64/xtables/libxt_TOS.so
/usr/lib64/xtables/libxt_TPROXY.so
/usr/lib64/xtables/libxt_TRACE.so
/usr/lib64/xtables/libxt_addrtype.so
/usr/lib64/xtables/libxt_bpf.so
/usr/lib64/xtables/libxt_cgroup.so
/usr/lib64/xtables/libxt_cluster.so
/usr/lib64/xtables/libxt_comment.so
/usr/lib64/xtables/libxt_connbytes.so
/usr/lib64/xtables/libxt_connlabel.so
/usr/lib64/xtables/libxt_connlimit.so
/usr/lib64/xtables/libxt_connmark.so
/usr/lib64/xtables/libxt_conntrack.so
/usr/lib64/xtables/libxt_cpu.so
/usr/lib64/xtables/libxt_dccp.so
/usr/lib64/xtables/libxt_devgroup.so
/usr/lib64/xtables/libxt_dscp.so
/usr/lib64/xtables/libxt_ecn.so
/usr/lib64/xtables/libxt_esp.so
/usr/lib64/xtables/libxt_hashlimit.so
/usr/lib64/xtables/libxt_helper.so
/usr/lib64/xtables/libxt_ipcomp.so
/usr/lib64/xtables/libxt_iprange.so
/usr/lib64/xtables/libxt_ipvs.so
/usr/lib64/xtables/libxt_length.so
/usr/lib64/xtables/libxt_limit.so
/usr/lib64/xtables/libxt_mac.so
/usr/lib64/xtables/libxt_mark.so
/usr/lib64/xtables/libxt_multiport.so
/usr/lib64/xtables/libxt_nfacct.so
/usr/lib64/xtables/libxt_osf.so
/usr/lib64/xtables/libxt_owner.so
/usr/lib64/xtables/libxt_physdev.so
/usr/lib64/xtables/libxt_pkttype.so
/usr/lib64/xtables/libxt_policy.so
/usr/lib64/xtables/libxt_quota.so
/usr/lib64/xtables/libxt_rateest.so
/usr/lib64/xtables/libxt_recent.so
/usr/lib64/xtables/libxt_rpfilter.so
/usr/lib64/xtables/libxt_sctp.so
/usr/lib64/xtables/libxt_set.so
/usr/lib64/xtables/libxt_socket.so
/usr/lib64/xtables/libxt_standard.so
/usr/lib64/xtables/libxt_state.so
/usr/lib64/xtables/libxt_statistic.so
/usr/lib64/xtables/libxt_string.so
/usr/lib64/xtables/libxt_tcp.so
/usr/lib64/xtables/libxt_tcpmss.so
/usr/lib64/xtables/libxt_time.so
/usr/lib64/xtables/libxt_tos.so
/usr/lib64/xtables/libxt_u32.so
/usr/lib64/xtables/libxt_udp.so

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libip4tc.so.2
/usr/lib32/libip4tc.so.2.0.0
/usr/lib32/libip6tc.so.2
/usr/lib32/libip6tc.so.2.0.0
/usr/lib32/libxtables.so.12
/usr/lib32/libxtables.so.12.2.0
/usr/lib32/xtables/libebt_among.so
/usr/lib32/xtables/libebt_arp.so
/usr/lib32/xtables/libebt_arpreply.so
/usr/lib32/xtables/libebt_dnat.so
/usr/lib32/xtables/libebt_ip6.so
/usr/lib32/xtables/libebt_pkttype.so
/usr/lib32/xtables/libebt_redirect.so
/usr/lib32/xtables/libebt_snat.so
/usr/lib32/xtables/libebt_stp.so
/usr/lib32/xtables/libebt_vlan.so
/usr/lib32/xtables/libip6t_srh.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/iptables/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/iptables-xml.1
/usr/share/man/man8/arptables-nft-restore.8
/usr/share/man/man8/arptables-nft-save.8
/usr/share/man/man8/arptables-nft.8
/usr/share/man/man8/ebtables-nft.8
/usr/share/man/man8/ip6tables-restore-translate.8
/usr/share/man/man8/ip6tables-restore.8
/usr/share/man/man8/ip6tables-save.8
/usr/share/man/man8/ip6tables-translate.8
/usr/share/man/man8/ip6tables.8
/usr/share/man/man8/iptables-extensions.8
/usr/share/man/man8/iptables-restore-translate.8
/usr/share/man/man8/iptables-restore.8
/usr/share/man/man8/iptables-save.8
/usr/share/man/man8/iptables-translate.8
/usr/share/man/man8/iptables.8
/usr/share/man/man8/nfnl_osf.8
/usr/share/man/man8/xtables-legacy.8
/usr/share/man/man8/xtables-monitor.8
/usr/share/man/man8/xtables-nft.8
/usr/share/man/man8/xtables-translate.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/ip6tables-restore.service
/usr/lib/systemd/system/ip6tables-save.service
/usr/lib/systemd/system/iptables-restore.service
/usr/lib/systemd/system/iptables-save.service

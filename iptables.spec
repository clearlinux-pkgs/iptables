#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : iptables
Version  : 1.4.21
Release  : 12
URL      : http://ftp.netfilter.org/pub/iptables/iptables-1.4.21.tar.bz2
Source0  : http://ftp.netfilter.org/pub/iptables/iptables-1.4.21.tar.bz2
Source1  : ip6tables-restore.service
Source2  : ip6tables-save.service
Source3  : iptables-restore.service
Source4  : iptables-save.service
Summary  : Interface to the (old) ip_queue mechanism
Group    : Development/Tools
License  : GPL-2.0
Requires: iptables-bin
Requires: iptables-config
Requires: iptables-lib
Requires: iptables-doc
Requires: iptables-data
BuildRequires : pkgconfig(libnetfilter_conntrack)
BuildRequires : pkgconfig(libnfnetlink)
Patch1: cve-2012-2663.patch
Patch2: test.patch

%description
No detailed description available

%package bin
Summary: bin components for the iptables package.
Group: Binaries
Requires: iptables-data
Requires: iptables-config

%description bin
bin components for the iptables package.


%package config
Summary: config components for the iptables package.
Group: Default

%description config
config components for the iptables package.


%package data
Summary: data components for the iptables package.
Group: Data

%description data
data components for the iptables package.


%package dev
Summary: dev components for the iptables package.
Group: Development
Requires: iptables-lib
Requires: iptables-bin
Requires: iptables-data
Provides: iptables-devel

%description dev
dev components for the iptables package.


%package doc
Summary: doc components for the iptables package.
Group: Documentation

%description doc
doc components for the iptables package.


%package extras
Summary: extras components for the iptables package.
Group: Default

%description extras
extras components for the iptables package.


%package lib
Summary: lib components for the iptables package.
Group: Libraries
Requires: iptables-data
Requires: iptables-config

%description lib
lib components for the iptables package.


%prep
%setup -q -n iptables-1.4.21
%patch1 -p1
%patch2 -p1

%build
export CFLAGS="$CFLAGS -Os -ffunction-sections "
export FCFLAGS="$CFLAGS -Os -ffunction-sections "
export FFLAGS="$CFLAGS -Os -ffunction-sections "
export CXXFLAGS="$CXXFLAGS -Os -ffunction-sections "
%configure --disable-static --enable-devel --enable-ipv6
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/ip6tables-restore.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/ip6tables-save.service
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/iptables-restore.service
install -m 0644 %{SOURCE4} %{buildroot}/usr/lib/systemd/system/iptables-save.service

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ip6tables
/usr/bin/ip6tables-restore
/usr/bin/ip6tables-save
/usr/bin/iptables
/usr/bin/iptables-restore
/usr/bin/iptables-save
/usr/bin/iptables-xml
/usr/bin/nfnl_osf
/usr/bin/xtables-multi

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/ip6tables-restore.service
/usr/lib/systemd/system/ip6tables-save.service
/usr/lib/systemd/system/iptables-restore.service
/usr/lib/systemd/system/iptables-save.service

%files data
%defattr(-,root,root,-)
/usr/share/xtables/pf.os

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/libiptc/ipt_kernel_headers.h
/usr/include/libiptc/libip6tc.h
/usr/include/libiptc/libiptc.h
/usr/include/libiptc/libxtc.h
/usr/include/libiptc/xtcshared.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man8/*

%files extras
%defattr(-,root,root,-)
/usr/lib64/libip4tc.so.0
/usr/lib64/libip4tc.so.0.1.0

%files lib
%defattr(-,root,root,-)
%exclude /usr/lib64/libip4tc.so.0
%exclude /usr/lib64/libip4tc.so.0.1.0
/usr/lib64/*.so.*
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
/usr/lib64/xtables/libipt_CLUSTERIP.so
/usr/lib64/xtables/libipt_DNAT.so
/usr/lib64/xtables/libipt_ECN.so
/usr/lib64/xtables/libipt_LOG.so
/usr/lib64/xtables/libipt_MASQUERADE.so
/usr/lib64/xtables/libipt_MIRROR.so
/usr/lib64/xtables/libipt_NETMAP.so
/usr/lib64/xtables/libipt_REDIRECT.so
/usr/lib64/xtables/libipt_REJECT.so
/usr/lib64/xtables/libipt_SAME.so
/usr/lib64/xtables/libipt_SNAT.so
/usr/lib64/xtables/libipt_TTL.so
/usr/lib64/xtables/libipt_ULOG.so
/usr/lib64/xtables/libipt_ah.so
/usr/lib64/xtables/libipt_icmp.so
/usr/lib64/xtables/libipt_realm.so
/usr/lib64/xtables/libipt_ttl.so
/usr/lib64/xtables/libipt_unclean.so
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

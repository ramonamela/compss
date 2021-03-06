
dnl Process this file with autoconf to produce a configure script.
AC_INIT()
AC_CONFIG_MACRO_DIR([m4])

AM_INIT_AUTOMAKE(all, 0.0.0)

AC_CANONICAL_HOST

AC_MSG_CHECKING([if we should activate AIX workarounds])
case $host_os in
	aix*)
		AC_MSG_RESULT([yes])
		CC=xlc
		CXX=xlC
		LD=xlC
		LDFLAGS="-brtl -bmaxdata:0x70000000"
		IS_AIX=yes
		AC_SUBST(IS_AIX)
		break;
		;;
	*)
		AC_MSG_RESULT([no])
		break;
		;;
esac
dnl Common config script configuration variables

dnl Checks for programs.
AC_PROG_CC
AC_PROG_CXX
AC_PROG_INSTALL

#AX_BOOST_BASE(1.54)
#AX_BOOST_SERIALIZATION

AC_PATH_PROG(COMPSSGEN, compss_generator, none)
if test x"$COMPSSGEN" = x"none" ; then
        AC_MSG_ERROR([Required compss_generator program missing.])
fi

dnl Initialize maintainer mode
AM_MAINTAINER_MODE
AC_ARG_WITH([cs-prefix],
	AS_HELP_STRING([  --with-cs-prefix=[prefix]], [Set the prefix under which the COMPSs Superscalar c library is installed.]),
	[
		LIBS=-L$withval/lib $LIBS
		CPPFLAGS="-I$withval/include $CPPFLAGS"
	]
)

dnl Linking with Nanos++ libraries if necessary
AC_ARG_WITH([ompss],
    AS_HELP_STRING([ --with-ompss], [Enables the use of OmpSs and specificates its directory.]),
            [
            ]
)

dnl Linking with Nanos6 libraries if necessary
AC_ARG_WITH([ompss-2],
    AS_HELP_STRING([ --with-ompss-2], [Enables the use of OmpSs-2 and specificates its directory.]),
            [
            #Nothing is needed!
            ]
)

dnl Checks for libraries.
#AC_CHECK_LIB(GS-master, GS_On,, [ AC_MSG_ERROR([Required Master COMP Supercalar c library cannot be found]) ])
#AC_CHECK_LIB(GS-worker, IniWorker,, [ AC_MSG_ERROR([Required Worker COMP Supercalar library cannot be found]) ])

dnl Checks for header files.
AC_HEADER_STDC
AC_CHECK_HEADERS(fcntl.h limits.h unistd.h)
#AC_CHECK_HEADERS(gs_base64.h, [], [AC_MSG_ERROR([COMP superscalar c header files could not be found])])

dnl Checks for typedefs, structures, and compiler characteristics.
AC_C_CONST
AC_TYPE_MODE_T
AC_TYPE_SIZE_T
AC_TYPE_SIGNAL

dnl Checks for library functions.
AC_CHECK_FUNCS(putenv socket strstr strtod)

AC_OUTPUT(Makefile)

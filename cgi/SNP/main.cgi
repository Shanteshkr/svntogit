#!/usr/local/bin/perl -T

###############################################################################
# Program     : main.cgi
# Author      : Eric Deutsch <edeutsch@systemsbiology.org>
# $Id$
#
# Description : This script authenticates the user, and then
#               displays the opening access page.
#
###############################################################################


###############################################################################
# Get the script set up with everything it will need
###############################################################################
use strict;
use vars qw ($q $sbeams $sbeamsSN $PROGRAM_FILE_NAME
             $current_contact_id $current_username);
use lib qw (../../lib/perl);
use CGI;
use CGI::Carp qw(fatalsToBrowser croak);

use SBEAMS::Connection;
use SBEAMS::Connection::Settings;

use SBEAMS::SNP;
use SBEAMS::SNP::Settings;

$q   = new CGI;
$sbeams = new SBEAMS::Connection;
$sbeamsSN = new SBEAMS::SNP;
$sbeamsSN->setSBEAMS($sbeams);


###############################################################################
# Global Variables
###############################################################################
$PROGRAM_FILE_NAME = 'main.cgi';
main();


###############################################################################
# Main Program:
#
# Call $sbeams->Authentication and stop immediately if authentication
# fails else continue.
###############################################################################
sub main { 

    #### Do the SBEAMS authentication and exit if a username is not returned
    exit unless ($current_username = $sbeams->Authenticate());

    #### Print the header, do what the program does, and print footer
    $sbeamsSN->printPageHeader();
    showMainPage();
    $sbeamsSN->printPageFooter();

} # end main


###############################################################################
# Show the main welcome page
###############################################################################
sub showMainPage {

    $sbeams->printUserContext();

    print qq!
	<BR>
	You are successfully logged into the $DBTITLE - $SBEAMS_PART system.
	Please choose your tasks from the menu bar on the left.<P>
	<BR>
	This system is still under active development.  Please be
	patient and report bugs, problems, difficulties, suggestions to
	<B>edeutsch\@systemsbiology.org</B>.<P>
	<BR>
	<BR>

	<UL>
	<LI> Here is the starter stub for the SNP area.
	</UL>

	<BR>
	<BR>
    !;

} # end showMainPage



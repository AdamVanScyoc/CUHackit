#!/usr/bin/perl

# merge existing diabetes data
my $completetext;

open (my $fh, '>>', 'datafull.txt');

foreach $x (qx / ls /) {
	if ( $x =~ /data/ )
	{
		#$completetext = qx / cat $x >> datafull.txt /;
		print $fh qx / cat $x /;
	}
}
close $fh;

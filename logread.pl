#!/usr/bin/perl -w
use warnings;

my $filename = shift or die "Usage: $0 <LOGFILE>\n";
open(my $fh, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";


while (my $row = <$fh>) {
  chomp $row;
  my @array = split(/ /, $row);
  if($array[6] =~ /(\.[a-z]{3}$)/i) {
    $count{$1}++;
  }

}

close($fh);

for(keys %count) {
  print "$_ - $count{$_}\n";
}

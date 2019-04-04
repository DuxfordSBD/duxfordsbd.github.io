#!/usr/bin/env perl
use strict;
use warnings;

use WWW::Mechanize;
use HTTP::Tiny;
use HTML::TreeBuilder 5 -weak;
use File::Spec;

my ($target_dir, $base_url) = @ARGV;

if(! -d $target_dir) {
  mkdir $target_dir or die "Cannot make ${target_dir}: $!";
}

my $mech = WWW::Mechanize->new();
$mech->get($base_url);
my $main_tree = HTML::TreeBuilder->new();
$main_tree->parse($mech->content());
$main_tree->eof();

my $http = HTTP::Tiny->new();
my @rows = $main_tree->find_by_tag_name('img');
my $unique_id = 1;
while(my $row = shift @rows) {
  my $image_url = $row->attr('data-orig-file');
  my $name;
  if($image_url =~ /\/([a-z0-9_.-]+\.jpg)$/) {
    $name = $1;
  }
  else {
    $name = $row->attr('data-image-title');
  }
  if($image_url) {
    my $response = $http->get($image_url);
    if($response->{success}) {
      print "Processing $name .... ";
      if($name !~ /\.jpg/) {
        $name .= '.jpg';
      }
      my $file = File::Spec->catfile($target_dir, ${name});
      if(-f $file) {
        $file = File::Spec->catfile($target_dir, "${unique_id}_${name}");
        $unique_id++;
      }
      print "writing to $file ... ";
      open my $fh, '>:raw', $file or die "Cannot open $file for writing: $!";
      print $fh $response->{content};
      close $fh;
      print "Done\n";
    }
  }
}

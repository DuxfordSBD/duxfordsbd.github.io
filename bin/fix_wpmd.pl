#!/usr/bin/env perl

####################################################
# Usage:
#   ./bin/fix_wpmd.pl new-markdown-post.md
#
# Installing dependencies:
#   cd bin && cpanm --installdeps . && cd ../
#
# Description:
#   Takes a markdown file converted by https://github.com/dreikanter/wp2md and
#   edits them into a format we expect for this blog. The code edits
#   markdown in place so make a backup of your original markdown export
#   before running this code.
#
####################################################

use strict;
use warnings;
use Tie::File;
use Text::Markdown;
use HTML::TreeBuilder 5 -weak;

my @to_remove = qw/
  link:
  author:
  post_id:
  created:
  created_gmt:
  comment_status:
  post_name:
  status:
  post_type:
/;

my ($file) = @ARGV;
if(!-f $file) {
  die "Cannot read $file";
}

tie my @array, 'Tie::File', $file or die "Cannot tie $file for fixing purposes";

# Find when we finish the key: value section. Just tmp scope to protect $length
{
  my $length = scalar(@array);
  my $index;
  for(my $i = 0; $i < $length; $i++) {
    if($array[$i] !~ /[a-z_]+:/) {
      $index = $i;
      last;
    }
  }
  # Splice the end front-matter at index and a new line at index+1
  splice(@array, $index++, 1, 'layout: page');
  splice(@array, $index++, 1, 'header: no');
  splice(@array, $index++, 1, 'categories:');
  splice(@array, $index++, 1, '    - news');
  splice(@array, $index++, 1, 'tags:');
  splice(@array, $index++, 1, '    - news');
  splice(@array, $index++, 1, '---');
  splice(@array, $index, 1, '');
  # Add start of front-matter to the markdown file
  unshift(@array, '---');
}

# Remove unwanted front-matter injected by the wpmd converter script
my $length = scalar(@array);
for(my $i = 0; $i < $length; $i++) {
  foreach my $remove (@to_remove) {
    if(index($array[$i], $remove) > -1) {
      splice(@array, $i, 1);
      $length--;
    }
  }
}

# Extract a teaser
my $markdown_content = q{};
my $in_front_matter = 0;
for(@array) {
  if($_ =~ /^---/) {
    if(!$in_front_matter) {
      $in_front_matter = 1;
    }
    else {
      $in_front_matter = 0;
    }
    next;
  }
  if(!$in_front_matter) {
    $markdown_content .= $_;
    $markdown_content .= "\n";
  }
}
my $m = Text::Markdown->new();
my $content = $m->markdown($markdown_content);
my $root = HTML::TreeBuilder->new();
$root->parse($content);
$root->eof();
my ($paragraph) = $root->find('p');
my $paragraph_content = $paragraph->as_text();
splice(@array, 1, 1, qq|teaser: "${paragraph_content}"|);
untie @array;
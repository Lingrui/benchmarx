#!/usr/bin/perl

if (scalar(@ARGV<2)){
	print "usage gold standard, prediction\n";
	die;
}


### read in gold standard and calculate default pe

($gs_file, $pred_file)=@ARGV;

$pos=0;
$neg=0;
open GS, $gs_file or die;
while ($line=<GS>){
	chomp $line;
	@table=split ",", $line;
	$ref{$table[0]}=$table[1];
	if ($table[1] == 1){
		$pos++;
	}else{
		$neg++;
	}
}
close GS;

$pos_ratio=$pos/($pos+$neg);
$neg_ratio=1-$pos_ratio;

$pe=$pos_ratio*$pos_ratio+$neg_ratio*$neg_ratio;

$correct=0;
$wrong=0;
open PRED, $pred_file or die;
while ($line=<PRED>){
	chomp $line;
	@table=split ",", $line;
	if ($table[1] == $ref{$table[0]}){
		$correct++;
	}else{
		$wrong++;
	}
}

$po=$correct/($correct+$wrong);
print "$po\n";

$kappa=($po-$pe)/(1-$pe);
print "$kappa\n";


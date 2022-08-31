{pkgs ? import <nixpkgs> {} }:
with pkgs;
let 
   mpkg = import ./python_shell.nix;
in 
pkgs.callPackage mpkg {}

{pkgs ? import <nixpkgs> {}}:
let 
    python = pkgs.python3.withPackages (p: with p; [
        numpy
        scipy
        matplotlib
        pytest
    ]);
in
pkgs.mkShell {
    buildInputs = [python];
}

{lib, buildPythonPackage, pytestCheckHook, matplotlib, numpy, pip, setuptools, pythonOlder }:

buildPythonPackage rec {
    pname = "render-anim";
    version = "0.0.1"; 
    disabled = pythonOlder "3.10";
    src = ./.;
    format = "pyproject";
    checkInputs = [ pytestCheckHook ];
    buildInputs = [pip setuptools]; 
    propagatedBuildInputs  = [ numpy matplotlib ];
    meta = with lib; {
    };
}


{
  description = "radar - simultaneous localization and mapping";
  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixos-24.11";
  outputs = { self, nixpkgs }:
    let system = "x86_64-linux";
        pkgs = import nixpkgs { inherit system; };
    in {
      # Used by `nix develop`
      devShells.${system}.default = pkgs.mkShell {
        name = "radar";
        nativeBuildInputs = [
          (pkgs.python3.withPackages (ps: with ps; [
            pysdl2 opencv-python scikit-image numpy 
          ]))
        ];
      };
    };
}

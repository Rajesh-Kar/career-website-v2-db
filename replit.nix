{ pkgs }: {
  systemPackages = with pkgs; [
    postgresql_13.dev
    postgresql_13.client
  ];
}

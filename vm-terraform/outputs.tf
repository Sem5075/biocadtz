output "output" {
  value = {
    machines = {
      for vm in proxmox_vm_qemu.machine :
      vm.name => {
        id  = vm.vmid
        ip  = vm.default_ipv4_address
      }
    }
  }
}
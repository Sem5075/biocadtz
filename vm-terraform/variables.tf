variable "vm_cores" {
  default = 2
}

variable "vm_memory" {
  default = 2048
}

variable "vm_disk" {
  type = string
  default = "20G"
}

variable "vm_prefix" {
  type = string
  default = "tzvm"
}

variable "vm_description" {
  type = string 
  default = "created via terraform"
}

variable "vm_id" {
  default = 160
}

variable "ci_user" {
  type = string
  sensitive = true
}

variable "ci_pass" {
  type = string
  sensitive = true
}

variable "proxmox_api_url" {
  type = string
}

variable "proxmox_api_token_id" {
  type = string
  sensitive = true
}

variable "proxmox_api_token_secret" {
  type = string
  sensitive = true
}

variable "ssh_public_key" {
  type    = string
  default = "~/.ssh/id_rsa.pub"
  sensitive = true
}

variable "vm_ip" {
  type        = string
  default     = "192.168.1.35/24"
}

variable "vm_gateway" {
  type        = string
  default     = "192.168.1.1"
}
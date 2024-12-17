import pytest
import json

from insights_api.src.rh_host import RHhost, RHsystemprofile


def test_creation():
    systemprofile_str = """{
      "count": 0,
      "page": 0,
      "per_page": 0,
      "total": 0,
      "results": [
        {
          "id": "string",
          "system_profile": {
            "ansible": {
              "catalog_worker_version": "1.2.3, 4.5.6, 7.8.9",
              "controller_version": "1.2.3, 4.5.6, 7.8.9",
              "hub_version": "1.2.3, 4.5.6, 7.8.9",
              "sso_version": "1.2.3, 4.5.6, 7.8.9"
            },
            "arch": "ARM, x86_64, RISC-V",
            "basearch": "x86_64, arm, ppc64",
            "bios_release_date": "ex1, ex2, ex3",
            "bios_vendor": "ex1, ex2, ex3",
            "bios_version": "ex1, ex2, ex3",
            "bootc_status": {
              "booted": {
                "cached_image": "quay.io/centos-bootc/fedora-bootc-cloud:eln, 192.168.0.1:5000/foo/foo:latest",
                "cached_image_digest": "sha256:806d77394f96e47cf99b1233561ce970c94521244a2d8f2affa12c3261961223, sha256:92e476435ced1c148350c660b09c744717defbd300a15d33deda5b50ad6b21a0",
                "image": "quay.io/centos-bootc/fedora-bootc-cloud:eln, 192.168.0.1:5000/foo/foo:latest",
                "image_digest": "sha256:806d77394f96e47cf99b1233561ce970c94521244a2d8f2affa12c3261961223, sha256:92e476435ced1c148350c660b09c744717defbd300a15d33deda5b50ad6b21a0"
              },
              "rollback": {
                "cached_image": "quay.io/centos-bootc/fedora-bootc-cloud:eln, 192.168.0.1:5000/foo/foo:latest",
                "cached_image_digest": "sha256:806d77394f96e47cf99b1233561ce970c94521244a2d8f2affa12c3261961223, sha256:92e476435ced1c148350c660b09c744717defbd300a15d33deda5b50ad6b21a0",
                "image": "quay.io/centos-bootc/fedora-bootc-cloud:eln, 192.168.0.1:5000/foo/foo:latest",
                "image_digest": "sha256:806d77394f96e47cf99b1233561ce970c94521244a2d8f2affa12c3261961223, sha256:92e476435ced1c148350c660b09c744717defbd300a15d33deda5b50ad6b21a0"
              },
              "staged": {
                "cached_image": "quay.io/centos-bootc/fedora-bootc-cloud:eln, 192.168.0.1:5000/foo/foo:latest",
                "cached_image_digest": "sha256:806d77394f96e47cf99b1233561ce970c94521244a2d8f2affa12c3261961223, sha256:92e476435ced1c148350c660b09c744717defbd300a15d33deda5b50ad6b21a0",
                "image": "quay.io/centos-bootc/fedora-bootc-cloud:eln, 192.168.0.1:5000/foo/foo:latest",
                "image_digest": "sha256:806d77394f96e47cf99b1233561ce970c94521244a2d8f2affa12c3261961223, sha256:92e476435ced1c148350c660b09c744717defbd300a15d33deda5b50ad6b21a0"
              }
            },
            "captured_date": "ex1, ex2, ex3",
            "cloud_provider": "aws, ms, ibm",
            "conversions": {
              "activity": true
            },
            "cores_per_socket": 2147483647,
            "cpu_flags": [
              "ex1, ex2, ex3"
            ],
            "cpu_model": "Intel(R) Xeon(R) CPU E5-2690 0 @ 2.90GHz, Intel(R) Xeon(R) CPU E9-7800 0 @ 1.90GHz, Intel(R) I7(R) CPU I7-10900k 0 @ 4.90GHz",
            "disk_devices": [
              {
                "device": "/dev/fdd0, /dev/sda1, /dev/nvme2",
                "label": "foo, bar, baz",
                "mount_point": "/mnt/remote_nfs_shares, /mnt/local_nfs, /mnt/foo",
                "options": {
                  "additionalProp1": "string",
                  "additionalProp2": "string",
                  "additionalProp3": "string"
                },
                "type": "ext1, ext2, ext3"
              }
            ],
            "dnf_modules": [
              {
                "name": "abc, dfg, pop",
                "stream": "abc, dfg, pop"
              }
            ],
            "enabled_services": [
              "ex1, ex2, ex3"
            ],
            "gpg_pubkeys": [
              "gpg-pubkey-11111111-22222222, gpg-pubkey-22222222-22222222, gpg-pubkey-22222222-33333333"
            ],
            "greenboot_fallback_detected": true,
            "greenboot_status": "green, red",
            "host_type": "edge, None",
            "image_builder": {
              "compliance_policy_id": "89b52baa-9912-4edc-9ed5-be15c06eaaa9",
              "compliance_profile_id": "xccdf_org.ssgproject.content_profile_cis"
            },
            "infrastructure_type": "physical, virtual, imaginary",
            "infrastructure_vendor": "ex1, ex2, baremetal",
            "insights_client_version": "3.0.1-2.el4_2, 5.0.6-2.el7_6, 6.0.6-2.el8_4",
            "insights_egg_version": "2.3, 4.4, 5.1",
            "installed_packages": [
              "krb5-libs-0:-1.16.1-23.fc29.i686, arb5-libs-0:-1.16.1-23.fc29.i686, brb5-libs-0:-1.16.1-23.fc29.i686"
            ],
            "installed_packages_delta": [
              "krb5-libs-0:-1.16.1-23.fc29.i686, arb5-libs-0:-1.16.1-23.fc29.i686, brb5-libs-0:-1.16.1-23.fc29.i686"
            ],
            "installed_products": [
              {
                "id": "abc, dfg, pop",
                "name": "abc, dfg, pop",
                "status": "Subscribed, inactive, canceled"
              }
            ],
            "installed_services": [
              "ex1, ex2, ex3"
            ],
            "intersystems": {
              "is_intersystems": true,
              "running_instances": [
                {
                  "instance_name": "IRIS3, PROD",
                  "product": "IRIS",
                  "version": "2023.1, 2023.2"
                }
              ]
            },
            "is_marketplace": true,
            "katello_agent_running": true,
            "kernel_modules": [
              "ex1, ex2, ex3"
            ],
            "last_boot_time": "2024-12-11T12:49:14.842Z",
            "mssql": {
              "version": "15.2.0, 12.5.3, 10.1.0"
            },
            "network_interfaces": [
              {
                "ipv4_addresses": [
                  "227.161.169.210 30.143.76.153 233.87.178.7, 60.209.47.155 40.124.217.134, 67.77.119.70"
                ],
                "ipv6_addresses": [
                  "8886:2565:f753:1bbb:1d08:4239:c470:a889, dd2e:879f:afff:7845:b346:bb88:bcf2:4b1b, e979:3081:7218:4c98:fd19:5777:309a:957b"
                ],
                "mac_address": "00:00:00:00:00:00, 100000000000, 20:00:00:00:00:00",
                "mtu": 2147483647,
                "name": "eth0, eth1, eth2",
                "state": "UP, DOWN, UNKNOWN",
                "type": "ether, infiniband, loopback"
              }
            ],
            "number_of_cpus": 2147483647,
            "number_of_sockets": 2147483647,
            "operating_system": {
              "major": 6,
              "minor": 8,
              "name": "RHEL, CentOS, CentOS Linux"
            },
            "os_kernel_version": "4.18.2, 4.5.0, 5.1.0",
            "os_release": "7.4, 8.2, 7.5",
            "owner_id": "22cd8e39-13bb-4d02-8316-84b850dc5136, ffdfd200-f5b9-4e57-b080-f5e257349df0, e2357169-f5e2-4afa-b509-ab1be3f30807",
            "public_dns": [
              "ec2-12-34-56-78.us-west-2.compute.amazonaws.com"
            ],
            "public_ipv4_addresses": [
              "12.23.31.32"
            ],
            "releasever": "7, 7.0, 7Server, 8, 8.4",
            "rhc_client_id": "22cd8e39-13bb-4d02-8316-84b850dc5136, 33cd8e39-13bb-4d02-8316-84b850dc5136, 2fa3e796-10e2-11ec-82a8-0242ac130003",
            "rhc_config_state": "22cd8e39-13bb-4d02-8316-84b850dc5136, 2c68e8ec-10e2-11ec-82a8-0242ac130003, 2fa3e796-10e2-11ec-82a8-0242ac130003",
            "rhel_ai": {
              "nvidia_gpu_models": [
                "Tesla V100-PCIE-16GB"
              ],
              "rhel_ai_version_id": "v1.1.3",
              "variant": "RHEL AI"
            },
            "rhsm": {
              "version": "8.1, 7.5, 9.9"
            },
            "rpm_ostree_deployments": [
              {
                "booted": true,
                "checksum": "63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb, 73335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb, 83335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
                "id": "fedora-silverblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0, fedora-blackpink-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0, fedora-orangeblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0",
                "origin": "fedora/33/x86_64/silverblue, fedora/31/x86_64/blackpink, fedora/34/x86_64/orangeblue",
                "osname": "fedora-silverblue, fedora-blackpink, fedora-orangeblue",
                "pinned": false,
                "version": "33.21, 31.12, 33.45"
              }
            ],
            "running_processes": [
              "ex1, ex2, ex3"
            ],
            "sap": {
              "instance_number": "03, 05, 99",
              "sap_system": true,
              "sids": [
                "H2O, ABC, XYZ"
              ],
              "version": "1.00.122.04.1478575636, 2.00.122.04.1478575636, 3.00.122.04.1478575636"
            },
            "sap_instance_number": "03, 05, 99",
            "sap_sids": [
              "H2O, ABC, XYZ"
            ],
            "sap_system": true,
            "sap_version": "1.00.122.04.1478575636, 2.00.122.04.1478575636, 3.00.122.04.1478575636",
            "satellite_managed": true,
            "selinux_config_file": "permissive, sleepy, authoritative",
            "selinux_current_mode": "enforcing, not_enforcing, sleeping",
            "subscription_auto_attach": "ex1, ex2, ex3",
            "subscription_status": "ex1, ex2, ex3",
            "system_memory_bytes": 9007199254740991,
            "system_purpose": {
              "role": "Red Hat Enterprise Linux Server, Red Hat Enterprise Linux Workstation, Red Hat Enterprise Linux Compute Node",
              "sla": "Premium, Standard, Self-Support",
              "usage": "Production, Development/Test, Disaster Recovery"
            },
            "system_update_method": "dnf, rpm-ostree, yum",
            "systemd": {
              "failed": 1,
              "failed_services": [
                "ex1, ex2, ex3"
              ],
              "jobs_queued": 4,
              "state": "initializing, starting, running, degraded, maintenance, stopping"
            },
            "third_party_services": {
              "crowdstrike": {
                "falcon_aid": "44e3b7d20b434a2bb2815d9808fa3a8b",
                "falcon_backend": "auto, kernel, bpf",
                "falcon_version": "7.14.16703.0, 6.33.13003.0"
              }
            },
            "threads_per_core": 2,
            "tuned_profile": "desktop, example, laptop",
            "virtual_host_uuid": "0ddf52cb-94e3-4ada-bdf7-d424a547b671, 6996463b-c9d4-402b-ad37-8ab5556ddf88, 0c352918-fa05-4f05-996c-6c43ec0b3c5e",
            "yum_repos": [
              {
                "base_url": "abc, dfg, pop",
                "enabled": true,
                "gpgcheck": true,
                "id": "abc, dfg, pop",
                "mirrorlist": "https://rhui.redhat.com/pulp/mirror/content/dist/rhel8/rhui/$releasever/$basearch/baseos/os",
                "name": "abc, dfg, pop"
              }
            ]
          }
        }
      ]
    }
    """

    host_str = """{
      "count": 0,
      "page": 0,
      "per_page": 0,
      "total": 0,
      "results": [
        {
          "bios_uuid": "22cd8e39-13bb-4d02-8316-84b850dc5136",
          "fqdn": "my.host.example.com",
          "insights_id": "3f01b55457674041b75e41829bcee1dc",
          "ip_addresses": [
            "10.10.0.1",
            "10.0.0.2"
          ],
          "mac_addresses": [
            "c2:00:d0:c8:61:01"
          ],
          "provider_id": "i-05d2313e6b9a42b16",
          "provider_type": "aws",
          "satellite_id": "22cd8e39-13bb-4d02-8316-84b850dc5136",
          "subscription_manager_id": "22cd8e39-13bb-4d02-8316-84b850dc5136",
          "ansible_host": "host1.mydomain.com",
          "created": "2024-12-11T12:59:41.204Z",
          "culled_timestamp": "2024-12-11T12:59:41.204Z",
          "display_name": "host1.mydomain.com",
          "facts": [
            {
              "facts": {
                "fact1": "value1",
                "fact2": "value2"
              },
              "namespace": "string"
            }
          ],
          "groups": [
            {
              "created": "2024-12-11T12:59:41.204Z",
              "id": "bA6deCFc19564430AB814bf8F70E8cEf",
              "name": "sre-group",
              "org_id": "000102",
              "updated": "2024-12-11T12:59:41.204Z"
            }
          ],
          "id": "3f01b55457674041b75e41829bcee1dc",
          "org_id": "000102",
          "per_reporter_staleness": {
            "additionalProp1": {
              "check_in_succeeded": true,
              "culled_timestamp": "2020-02-10T08:07:03.354307+00:00",
              "last_check_in": "2020-02-10T08:07:03.354307+00:00",
              "stale_timestamp": "2020-02-10T08:07:03.354307+00:00",
              "stale_warning_timestamp": "2020-02-10T08:07:03.354307+00:00"
            },
            "additionalProp2": {
              "check_in_succeeded": true,
              "culled_timestamp": "2020-02-10T08:07:03.354307+00:00",
              "last_check_in": "2020-02-10T08:07:03.354307+00:00",
              "stale_timestamp": "2020-02-10T08:07:03.354307+00:00",
              "stale_warning_timestamp": "2020-02-10T08:07:03.354307+00:00"
            },
            "additionalProp3": {
              "check_in_succeeded": true,
              "culled_timestamp": "2020-02-10T08:07:03.354307+00:00",
              "last_check_in": "2020-02-10T08:07:03.354307+00:00",
              "stale_timestamp": "2020-02-10T08:07:03.354307+00:00",
              "stale_warning_timestamp": "2020-02-10T08:07:03.354307+00:00"
            }
          },
          "reporter": "string",
          "stale_timestamp": "2024-12-11T12:59:41.204Z",
          "stale_warning_timestamp": "2024-12-11T12:59:41.204Z",
          "system_profile": {
            "ansible": {
              "catalog_worker_version": "1.2.3, 4.5.6, 7.8.9",
              "controller_version": "1.2.3, 4.5.6, 7.8.9",
              "hub_version": "1.2.3, 4.5.6, 7.8.9",
              "sso_version": "1.2.3, 4.5.6, 7.8.9"
            },
            "arch": "ARM, x86_64, RISC-V",
            "basearch": "x86_64, arm, ppc64",
            "bios_release_date": "ex1, ex2, ex3",
            "bios_vendor": "ex1, ex2, ex3",
            "bios_version": "ex1, ex2, ex3",
            "bootc_status": {
              "booted": {
                "cached_image": "quay.io/centos-bootc/fedora-bootc-cloud:eln, 192.168.0.1:5000/foo/foo:latest",
                "cached_image_digest": "sha256:806d77394f96e47cf99b1233561ce970c94521244a2d8f2affa12c3261961223, sha256:92e476435ced1c148350c660b09c744717defbd300a15d33deda5b50ad6b21a0",
                "image": "quay.io/centos-bootc/fedora-bootc-cloud:eln, 192.168.0.1:5000/foo/foo:latest",
                "image_digest": "sha256:806d77394f96e47cf99b1233561ce970c94521244a2d8f2affa12c3261961223, sha256:92e476435ced1c148350c660b09c744717defbd300a15d33deda5b50ad6b21a0"
              },
              "rollback": {
                "cached_image": "quay.io/centos-bootc/fedora-bootc-cloud:eln, 192.168.0.1:5000/foo/foo:latest",
                "cached_image_digest": "sha256:806d77394f96e47cf99b1233561ce970c94521244a2d8f2affa12c3261961223, sha256:92e476435ced1c148350c660b09c744717defbd300a15d33deda5b50ad6b21a0",
                "image": "quay.io/centos-bootc/fedora-bootc-cloud:eln, 192.168.0.1:5000/foo/foo:latest",
                "image_digest": "sha256:806d77394f96e47cf99b1233561ce970c94521244a2d8f2affa12c3261961223, sha256:92e476435ced1c148350c660b09c744717defbd300a15d33deda5b50ad6b21a0"
              },
              "staged": {
                "cached_image": "quay.io/centos-bootc/fedora-bootc-cloud:eln, 192.168.0.1:5000/foo/foo:latest",
                "cached_image_digest": "sha256:806d77394f96e47cf99b1233561ce970c94521244a2d8f2affa12c3261961223, sha256:92e476435ced1c148350c660b09c744717defbd300a15d33deda5b50ad6b21a0",
                "image": "quay.io/centos-bootc/fedora-bootc-cloud:eln, 192.168.0.1:5000/foo/foo:latest",
                "image_digest": "sha256:806d77394f96e47cf99b1233561ce970c94521244a2d8f2affa12c3261961223, sha256:92e476435ced1c148350c660b09c744717defbd300a15d33deda5b50ad6b21a0"
              }
            },
            "captured_date": "ex1, ex2, ex3",
            "cloud_provider": "aws, ms, ibm",
            "conversions": {
              "activity": true
            },
            "cores_per_socket": 2147483647,
            "cpu_flags": [
              "ex1, ex2, ex3"
            ],
            "cpu_model": "Intel(R) Xeon(R) CPU E5-2690 0 @ 2.90GHz, Intel(R) Xeon(R) CPU E9-7800 0 @ 1.90GHz, Intel(R) I7(R) CPU I7-10900k 0 @ 4.90GHz",
            "disk_devices": [
              {
                "device": "/dev/fdd0, /dev/sda1, /dev/nvme2",
                "label": "foo, bar, baz",
                "mount_point": "/mnt/remote_nfs_shares, /mnt/local_nfs, /mnt/foo",
                "options": {
                  "additionalProp1": "string",
                  "additionalProp2": "string",
                  "additionalProp3": "string"
                },
                "type": "ext1, ext2, ext3"
              }
            ],
            "dnf_modules": [
              {
                "name": "abc, dfg, pop",
                "stream": "abc, dfg, pop"
              }
            ],
            "enabled_services": [
              "ex1, ex2, ex3"
            ],
            "gpg_pubkeys": [
              "gpg-pubkey-11111111-22222222, gpg-pubkey-22222222-22222222, gpg-pubkey-22222222-33333333"
            ],
            "greenboot_fallback_detected": true,
            "greenboot_status": "green, red",
            "host_type": "edge, None",
            "image_builder": {
              "compliance_policy_id": "89b52baa-9912-4edc-9ed5-be15c06eaaa9",
              "compliance_profile_id": "xccdf_org.ssgproject.content_profile_cis"
            },
            "infrastructure_type": "physical, virtual, imaginary",
            "infrastructure_vendor": "ex1, ex2, baremetal",
            "insights_client_version": "3.0.1-2.el4_2, 5.0.6-2.el7_6, 6.0.6-2.el8_4",
            "insights_egg_version": "2.3, 4.4, 5.1",
            "installed_packages": [
              "krb5-libs-0:-1.16.1-23.fc29.i686, arb5-libs-0:-1.16.1-23.fc29.i686, brb5-libs-0:-1.16.1-23.fc29.i686"
            ],
            "installed_packages_delta": [
              "krb5-libs-0:-1.16.1-23.fc29.i686, arb5-libs-0:-1.16.1-23.fc29.i686, brb5-libs-0:-1.16.1-23.fc29.i686"
            ],
            "installed_products": [
              {
                "id": "abc, dfg, pop",
                "name": "abc, dfg, pop",
                "status": "Subscribed, inactive, canceled"
              }
            ],
            "installed_services": [
              "ex1, ex2, ex3"
            ],
            "intersystems": {
              "is_intersystems": true,
              "running_instances": [
                {
                  "instance_name": "IRIS3, PROD",
                  "product": "IRIS",
                  "version": "2023.1, 2023.2"
                }
              ]
            },
            "is_marketplace": true,
            "katello_agent_running": true,
            "kernel_modules": [
              "ex1, ex2, ex3"
            ],
            "last_boot_time": "2024-12-11T12:59:41.204Z",
            "mssql": {
              "version": "15.2.0, 12.5.3, 10.1.0"
            },
            "network_interfaces": [
              {
                "ipv4_addresses": [
                  "227.161.169.210 30.143.76.153 233.87.178.7, 60.209.47.155 40.124.217.134, 67.77.119.70"
                ],
                "ipv6_addresses": [
                  "8886:2565:f753:1bbb:1d08:4239:c470:a889, dd2e:879f:afff:7845:b346:bb88:bcf2:4b1b, e979:3081:7218:4c98:fd19:5777:309a:957b"
                ],
                "mac_address": "00:00:00:00:00:00, 100000000000, 20:00:00:00:00:00",
                "mtu": 2147483647,
                "name": "eth0, eth1, eth2",
                "state": "UP, DOWN, UNKNOWN",
                "type": "ether, infiniband, loopback"
              }
            ],
            "number_of_cpus": 2147483647,
            "number_of_sockets": 2147483647,
            "operating_system": {
              "major": 6,
              "minor": 8,
              "name": "RHEL, CentOS, CentOS Linux"
            },
            "os_kernel_version": "4.18.2, 4.5.0, 5.1.0",
            "os_release": "7.4, 8.2, 7.5",
            "owner_id": "22cd8e39-13bb-4d02-8316-84b850dc5136, ffdfd200-f5b9-4e57-b080-f5e257349df0, e2357169-f5e2-4afa-b509-ab1be3f30807",
            "public_dns": [
              "ec2-12-34-56-78.us-west-2.compute.amazonaws.com"
            ],
            "public_ipv4_addresses": [
              "12.23.31.32"
            ],
            "releasever": "7, 7.0, 7Server, 8, 8.4",
            "rhc_client_id": "22cd8e39-13bb-4d02-8316-84b850dc5136, 33cd8e39-13bb-4d02-8316-84b850dc5136, 2fa3e796-10e2-11ec-82a8-0242ac130003",
            "rhc_config_state": "22cd8e39-13bb-4d02-8316-84b850dc5136, 2c68e8ec-10e2-11ec-82a8-0242ac130003, 2fa3e796-10e2-11ec-82a8-0242ac130003",
            "rhel_ai": {
              "nvidia_gpu_models": [
                "Tesla V100-PCIE-16GB"
              ],
              "rhel_ai_version_id": "v1.1.3",
              "variant": "RHEL AI"
            },
            "rhsm": {
              "version": "8.1, 7.5, 9.9"
            },
            "rpm_ostree_deployments": [
              {
                "booted": true,
                "checksum": "63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb, 73335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb, 83335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
                "id": "fedora-silverblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0, fedora-blackpink-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0, fedora-orangeblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0",
                "origin": "fedora/33/x86_64/silverblue, fedora/31/x86_64/blackpink, fedora/34/x86_64/orangeblue",
                "osname": "fedora-silverblue, fedora-blackpink, fedora-orangeblue",
                "pinned": false,
                "version": "33.21, 31.12, 33.45"
              }
            ],
            "running_processes": [
              "ex1, ex2, ex3"
            ],
            "sap": {
              "instance_number": "03, 05, 99",
              "sap_system": true,
              "sids": [
                "H2O, ABC, XYZ"
              ],
              "version": "1.00.122.04.1478575636, 2.00.122.04.1478575636, 3.00.122.04.1478575636"
            },
            "sap_instance_number": "03, 05, 99",
            "sap_sids": [
              "H2O, ABC, XYZ"
            ],
            "sap_system": true,
            "sap_version": "1.00.122.04.1478575636, 2.00.122.04.1478575636, 3.00.122.04.1478575636",
            "satellite_managed": true,
            "selinux_config_file": "permissive, sleepy, authoritative",
            "selinux_current_mode": "enforcing, not_enforcing, sleeping",
            "subscription_auto_attach": "ex1, ex2, ex3",
            "subscription_status": "ex1, ex2, ex3",
            "system_memory_bytes": 9007199254740991,
            "system_purpose": {
              "role": "Red Hat Enterprise Linux Server, Red Hat Enterprise Linux Workstation, Red Hat Enterprise Linux Compute Node",
              "sla": "Premium, Standard, Self-Support",
              "usage": "Production, Development/Test, Disaster Recovery"
            },
            "system_update_method": "dnf, rpm-ostree, yum",
            "systemd": {
              "failed": 1,
              "failed_services": [
                "ex1, ex2, ex3"
              ],
              "jobs_queued": 4,
              "state": "initializing, starting, running, degraded, maintenance, stopping"
            },
            "third_party_services": {
              "crowdstrike": {
                "falcon_aid": "44e3b7d20b434a2bb2815d9808fa3a8b",
                "falcon_backend": "auto, kernel, bpf",
                "falcon_version": "7.14.16703.0, 6.33.13003.0"
              }
            },
            "threads_per_core": 2,
            "tuned_profile": "desktop, example, laptop",
            "virtual_host_uuid": "0ddf52cb-94e3-4ada-bdf7-d424a547b671, 6996463b-c9d4-402b-ad37-8ab5556ddf88, 0c352918-fa05-4f05-996c-6c43ec0b3c5e",
            "yum_repos": [
              {
                "base_url": "abc, dfg, pop",
                "enabled": true,
                "gpgcheck": true,
                "id": "abc, dfg, pop",
                "mirrorlist": "https://rhui.redhat.com/pulp/mirror/content/dist/rhel8/rhui/$releasever/$basearch/baseos/os",
                "name": "abc, dfg, pop"
              }
            ]
          },
          "updated": "2024-12-11T12:59:41.204Z"
        }
      ]
    }"""

    systemprofile_json = json.loads(systemprofile_str)
    host_json = json.loads(host_str)

    try:
        tmp = host_json["results"][0]
        rhhost_obj = RHhost(
            id=tmp["id"],
            insights_id=tmp["insights_id"],
            fqdn=tmp["fqdn"],
            display_name=tmp["display_name"],
            org_id=tmp["org_id"],
        )
        rhhost_obj.systemprofile = RHsystemprofile(**systemprofile_json["results"][0])

    except Exception as e:
        assert False, f"Error occured which should have not: {e}"

    print(rhhost_obj.id)
    assert rhhost_obj.id == host_json["results"][0]["id"]

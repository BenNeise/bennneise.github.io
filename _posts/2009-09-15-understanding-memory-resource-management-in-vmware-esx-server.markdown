---
layout: post
title: Understanding memory resource management in VMware ESX
date: '2009-09-15 13:23:28'
tags:
- memory
- virtualisation
- vsphere
---

VMware have published an excellent [white paper on memory management](http://www.vmware.com/files/pdf/perf-vsphere-memory_management.pdf) [pdf].

The document is technically detailed, but makes interesting reading. The authors do a good job of describing the methods ESX uses to manage and allocate virtual memory; and how when guests deallocate memory it's not necessarily freed up for reuse by other guests. This should prevent you from allocating more memory to guests than is physically available on the host (overcommitting); however the hypervisor uses three memory reclamation strategies which allow overcommitment:-

- **Transparent Page Sharing (TPS).** Where ESX detects that multiple guests are using identical memory pages (such as those used by common OS components), it presents one shared copy to the guests. By default, this is active all the time. If the guests need to write to the memory, a copy needs to be made, which incurs a slight performance penalty.
- **Ballooning**. Is where VMware tools allows the hypervisor to see inside the guest operating system and reclaim unused memory. This typically occurs when ESX drops to less than 4% free memory (the *Soft* threshold). It has more of an overhead than TPS, but is still preferable to the alternative.
- **Hypervisor swapping**. This is used as a last-resort when TPS or Ballooning cannot provide enough memory (or cannot provide it quickly enough). Swapping tends to affect the guest more than the other two methods.

In the unlikely event that Hypervisor Swapping is unable to provide enough memory to meet the requirement, the hypervisor blocks the execution of all virtual machines which exceed their memory limit.

The whitepaper details the results of various benchmarks to evaluate the performance overhead of each of the reclamation strategies. While I'd certainly heard that the performance impact of TPS was negligible, I had always been slightly sceptical, but the data provided by VMware would appear to back it up.

The whitepaper also includes some best practices for memory management, some of which have had me thinking about our memory allocation strategy:-

- **Do not disable page sharing or the balloon driver**. These two techniques are enabled by default in ESX4 and I can't imagine that anyone would disable them unless they had specific reason to. It's also another reason to make sure you have VMware tools installed on all your guests.
- **Carefully specify the memory limit and memory reservation**. Our environment is pretty fluid, with a large number of small guests with 10-15% of them being used. For this to be useful for us, these values would need to be constantly checked and reconfigured.
- **Host memory size should be larger than guest memory usage**. I generally try to limit our hosts to a 20% potential overcommit on RAM allocated to guests, and as there are usually only about 80% of our machines switched on at any one time, the hosts are normally pretty comfortable. However, this conservative approach means our RAM allocations need to be carefully managed, and kept as low as possible; which may be hitting us elsewhere (see below)
- **Use shares to adjust relative priorities when memory is overcommitted**. Our environment is pretty unique in that the vast majority of the machines have equal priority, so there's little need for us to add another management overhead.
- **Set appropriate Virtual Machine memory size**. The virtual machine memory size should be a little larger than the average used by the guest. I think this is an area we need to look at in our environment. Our default RAM allocations for guests is probably a little on the low side, due to historical reasons, and due to our current environment being configured with a  rather paltry 16GB of physical RAM (a problem that will be resolved in the next couple of months). We may be keeping our memory usage in check, but the resultant disk-swapping might be stressing our storage infrastructure.

The white paper is definitely worth reading; it's certainly going to help me plan a memory management strategy for the implementing our infrastructure on the new hardware .



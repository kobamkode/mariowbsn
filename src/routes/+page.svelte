<script lang="ts">
  const exps = [
    {
      company: 'Musang Teknologi Nusantara',
      role: 'Fullstack Programmer',
      start: '2025',
      end: 'Present',
      description:
        'Built a multi-tenant fuel monitoring platform from the ground up, delivering real-time metrics from embedded fuel systems across multiple organizations. Championed DevOps practices that streamlined deployments and improved overall system reliability.',
      stacks: ['typescript', 'golang', 'azure']
    },
    {
      company: 'The Indonesia Capital Market Institute (TICMI)',
      role: 'Fullstack Programmer',
      start: '2021',
      end: '2025',
      description:
        "Engineered critical features for a Learning Management System serving thousands of students, and led the end-to-end integration with PRAKERJA (Indonesia's government-backed job training program) expanding platform reach and unlocking new revenue streams.",
      stacks: ['laravel', 'gcp']
    },
    {
      company: 'Global Tiket Network (Tiket)',
      role: 'Site Reliability Engineer',
      start: '2018',
      end: '2021',
      description:
        "Safeguarded platform resilience for one of Indonesia's largest travel marketplaces by designing and executing comprehensive load tests, proactively identifying bottlenecks and ensuring seamless performance during peak traffic events.",
      stacks: ['prometheus', 'k6', 'gcp']
    },
    {
      company: 'Visionet Internasional (OVO)',
      role: 'Site Reliability Engineer',
      start: 2018,
      end: 2018,
      description:
        "Designed and implemented a real-time observability system using Grafana and Prometheus for one of Indonesia's leading digital payment platforms, enabling proactive incident detection and significantly reducing potential downtime.",
      stacks: ['prometheus', 'golang']
    },
    {
      company: 'MBDC Media (MalesBanget)',
      role: 'Fullstack Programmer',
      start: 2015,
      end: 2018,
      description:
        "Led a full platform migration from WordPress to a custom-built system, dramatically improving performance and scalability. Delivered user-facing features and developed multiple agency microsites, strengthening the brand's digital footprint.",
      stacks: ['python', 'aws']
    }
  ];
</script>

<!-- HERO -->
<div class="p-4">
  <p class="py-4 font-poppins text-2xl">👋 Hello!</p>
  <p class="font-fraunces text-5xl leading-14 font-semibold">
    I'm <span class="underline decoration-amber-600">Mario</span> a fullstack programmer from Indonesia.
  </p>
</div>

<!-- WORKING EXPERIENCES -->
<div class="p-4">
  <p class="py-4 font-poppins text-2xl">🧑‍💻 Working Experiences</p>
  {#each exps as exp (exp.company)}
    <div
      class="flex flex-col gap-4 border-b border-b-gray-600
      py-4"
    >
      <div class="flex flex-col gap-2">
        <p class="font-poppins text-2xl font-semibold">{exp.company}</p>
        <p class="font-poppins font-semibold">{exp.role}</p>
        <p class="font-poppins text-sm">{exp.start} - {exp.end}</p>
      </div>
      <div class="flex flex-col gap-4 py-4">
        <p>{exp.description}</p>
        <div class="flex gap-4">
          {#each exp.stacks as stack (stack)}
            <p class="rounded-full bg-amber-600 px-4 py-2">{stack}</p>
          {/each}
        </div>
      </div>
    </div>
  {/each}
</div>

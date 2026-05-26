<script lang="ts">
  const workExps = [
    {
      company: 'Musang Teknologi Nusantara',
      start: '2025',
      end: 'Present',
      description: 'As software engineer focus on cloud',
      stacks: ['typescript', 'golang', 'azure']
    },
    {
      company: 'The Indonesia Capital Market Institute (TICMI)',
      start: '2021',
      end: '2025',
      description: 'As software engineer focus on cloud',
      stacks: ['laravel', 'gcp']
    },
    {
      company: 'Global Tiket Network (Tiket)',
      start: '2018',
      end: '2021',
      description: 'As software engineer focus on cloud',
      stacks: ['prometheus', 'k6', 'gcp']
    },
    {
      company: 'Visionet Internasional (OVO)',
      start: 2018,
      end: 2018,
      description: 'As software engineer focus on cloud',
      stacks: ['prometheus', 'golang']
    },
    {
      company: 'MBDC Media (MalesBanget)',
      start: 2015,
      end: 2018,
      description: 'As software engineer focus on cloud',
      stacks: ['python', 'aws']
    }
  ];
</script>

<!-- HERO -->
<div class="p-4">
  <p class="py-4 font-poppins text-2xl">👋 Hello</p>
  <p class="font-fraunces text-5xl leading-14 font-semibold">
    I'm <span class="underline decoration-amber-600">Mario</span> a fullstack developer from Indonesia.
  </p>
</div>

<!-- WORKING EXPERIENCES -->
<div class="p-4">
  <p class="py-4 font-poppins text-2xl">🧑‍💻 Working Experiences</p>
  {#each workExps as exp (exp.company)}
    <div
      class="flex flex-col gap-4 border-b border-b-gray-600
      py-4"
    >
      <div>
        <p class="font-poppins text-2xl font-semibold">{exp.company}</p>
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

+++
date = '2026-07-21T07:33:51+07:00'
draft = false
title = 'How I Approached Persistent Storage in Docker with RustFS'
summary = 'A look at how I solved persistent file storage in containerized applications using RustFS.'
description = 'A look at how I solved persistent file storage in containerized applications using RustFS.'
+++

As software engineers, we often save images, audio, and video files alongside our application in a server. While this approach is convenient during development, it becomes problematic in production. Since I've moved to a fully containerized deployment, any files saved within a container are lost when a new container is deployed. To solve this, I'm separating uploads to a dedicated storage solution.

Several object storage options are available: S3, Google Cloud Storage, Azure Blob Storage, and others, each with different pricing models to consider. In a containerized environment, I could run an S3 compatible object storage like MinIO, but unfortunately their GitHub repository is no longer maintained. Fortunately, there's an excellent alternative called RustFS.

I run RustFS behind Traefik and Cloudflare for public access with authentication enabled. RustFS provides two url endpoints, one for accessing objects and another for the web console. The RustFS console is a dashboard for managing buckets, IAM, and other settings, it can be enabled or disabled during setup via environment variables. Another advantage is that you can use any existing S3 client library, so there's no need to refactor code if you already use S3.

With dedicated object storage in place, managing multimedia and scaling becomes straightforward without straining the application server.

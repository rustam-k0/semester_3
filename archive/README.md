# Historical study archive

User-supplied collection of older Medieninformatik examination papers, practice materials, lecture documents, literature and exercise projects.

The original internal folder structure and filenames are preserved. `Dateinamen-Zuordnung.tsv` records filename mappings supplied with the collection. `Meine Pruefungsmaterialien` contains a selected collection; `Medieninformatik Bachelor` contains the broader archive. Files may overlap between these collections.

These materials are historical references. Their relevance to current courses, tracks and assessment rules has not been verified. Semester and teacher labels describe the archived sources and do not establish current track assignments.

This archive is kept outside the application and is not imported into its databases. Workspace filename normalization and deduplication rules do not apply inside this archive; preserve its existing contents and structure.

## GitHub storage and recovery

Both original collection folders are stored with Git LFS, including the historical exercise projects and their bundled files. Names and bytes are preserved; identical contents share LFS storage without removing any original paths. The collection's README and filename mapping remain ordinary Git files.

To restore the complete collection, install Git LFS, run `git lfs install`, clone the repository, and run `git lfs pull` from the checkout. A checkout made with LFS downloads disabled contains small pointer files until `git lfs pull` downloads the originals. Downloading a source ZIP is not a reliable substitute unless GitHub is configured to include LFS objects.

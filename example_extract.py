#!/usr/bin/env python3
import json, zipfile, sys, os

# thrown together example on extracting files from chunks
# this is an example only, do not use this for anything serious as zipfile is very slow
# chunk max size is always 1MB (2*20) so far, so chunk size and offset are ignored

def extract(files, zipf, path, f):
    out = f"{path}/{f}"

    # handle directories
    if files[f]["flags"] & 64:
        os.makedirs(out, exist_ok=True)
        return

    # handle files
    try:
        total = len(files[f]["chunks"])
        cur = 0
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "wb") as outf:
            # append each chunk in order to the output file
            for c in files[f]["chunks"]:
                cur += 1
                progress = f"#{cur}/{total} {f}"
                print(progress + (" " * (os.get_terminal_size()[0] - len(progress))), end="\r")

                # ignore if chunk is empty
                if c == "0000000000000000000000000000000000000000":
                    break

                outf.write(zipf.read(f"{c[0:2]}/{c}"))
    except Exception as e:
        print(f"Failed to extract file {f}")
        print(e)
        sys.exit(1)

def main(args):
    try:
        archive = args[0]
        depot_id = int(args[1])
        manifest_id = int(args[2])
    except:
        print(f"Bad arguments: {args[0:3]}")
        sys.exit(1)

    if len(args) > 3:
        root = args[3]
    else:
        root = ""

    if len(args) > 4:
        path = args[4]
    else:
        path = f"{depot_id}/{manifest_id}"

    try:
        with zipfile.ZipFile(f"manifests_{archive}.zip") as zipf:
            with zipf.open(f"{depot_id}/{manifest_id}.json") as f:
                manifest = json.load(f)
    except:
        print(f"Failed to open manifest {depot_id}/{manifest_id}.json from archive manifests_{archive}.zip")
        sys.exit(1)

    print(f"Extracting from {manifest['name']} v{manifest_id}")

    try:
        chunks = zipfile.ZipFile(f"chunks_{archive}.zip")
        os.makedirs(path, exist_ok=True)
    except:
        print(f"Failed to open chunks archive chunks_{archive}.zip")
        sys.exit(1)

    for f in manifest["files"]:
        if f.startswith(root):
            extract(manifest["files"], chunks, path, f)

    print("")

if __name__ == "__main__":
    if len(sys.argv) not in [4, 5, 6]:
        print(f"Usage: {sys.argv[0]} archive_name depot_id manifest_id [path_filter] [output_path]"
                "\nExamples:\n"
                f"\t{sys.argv[0]} tf2 441 5 tf/maps/ tf2_maps\n"
                f"\t{sys.argv[0]} engine 216 0")
        sys.exit()
    main(sys.argv[1:])

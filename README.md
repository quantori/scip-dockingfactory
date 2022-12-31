# DockingFactory 

Copyright (c) 2022 Quantori.

Docking Factory is a command line tool to automate molecular docking runs on an HPC cluster using the Dask framework. 

See the [DockingFactory Bundle](https://github.com/quantori/scip-dockingfactory-bundle) repo for detailed information.

## Bundle

DockingFactory is usually installed as part of [Quantori DockingFactory Bundle](https://github.com/quantori/scip-dockingfactory-bundle). Other projects that are also parts of the bundle are:
- [DockingInterface](https://github.com/quantori/scip-dockinginterface)
- [Vina](https://github.com/quantori/scip-vina)
- [Smina](https://github.com/quantori/scip-smina)
- [QVina 2](https://github.com/quantori/scip-qvina)
- [rDock](https://github.com/quantori/scip-rdock)

## Installation

See the [DockingFactory Bundle](https://github.com/quantori/scip-dockingfactory-bundle) repo for installation instructions.

## Quick Start

```
cd tests/test1local
dockingfactory.py --config config.yml --local yes
```

## Usage

```
usage: dockingfactory.py [-h] [--config CONFIG] [--handler HANDLER]
                         [--handler_config HANDLER_CONFIG]
                         [--input_path INPUT_PATH] [--receptor RECEPTOR]
                         [--output_folder OUTPUT_FOLDER]
                         [--rdock_protocol RDOCK_PROTOCOL]
                         [--rdock_recdef RDOCK_RECDEF]
                         [--rdock_nruns RDOCK_NRUNS] [--rdock_root RDOCK_ROOT]
                         [--rdock_home RDOCK_HOME] [--csv_out CSV_OUT]
                         [--output OUTPUT] [--address ADDRESS]
                         [--maximum_scale MAXIMUM_SCALE] [--name NAME]
                         [--partition PARTITION]
                         [--worker_instance_type WORKER_INSTANCE_TYPE]
                         [--scheduler_instance_type SCHEDULER_INSTANCE_TYPE]
                         [--server_mode SERVER_MODE]
                         [--failed_ligand_out FAILED_LIGAND_OUT]
                         [--error_msg_out ERROR_MSG_OUT]
                         [--errors_aws ERRORS_AWS] [--restart RESTART]
                         [--cost_per_cpu COST_PER_CPU] [--debug DEBUG]
                         [--local LOCAL]

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Main config file (.yml)
  --handler HANDLER     Name of handler (usually smina)
  --handler_config HANDLER_CONFIG
                        Path to config file for handler (.txt)
  --input_path INPUT_PATH
                        Path to folder with ligands (.pdbqt, subdirectories
                        are searched automatically)
  --receptor RECEPTOR   Path to receptor (.pdbqt)
  --output_folder OUTPUT_FOLDER
                        Path to output folder for docked .pdbqt
  --rdock_protocol RDOCK_PROTOCOL
                        Protocol for rDock (.prm)
  --rdock_recdef RDOCK_RECDEF
                        Receptor definition for rDock (.prm)
  --rdock_nruns RDOCK_NRUNS
                        Number of runs for rdock
  --rdock_root RDOCK_ROOT
                        Root directory of rDock files
  --rdock_home RDOCK_HOME
                        Home directory of rDock files
  --csv_out CSV_OUT     Path to output .csv file
  --output OUTPUT       Path to output folder with .csv, ligands, errors, and
                        etc.
  --address ADDRESS     Dask cluster address
  --maximum_scale MAXIMUM_SCALE
                        Dask cluster maximum scale
  --name NAME           Dask cluster name
  --partition PARTITION
                        Partition for Dask cluster
  --worker_instance_type WORKER_INSTANCE_TYPE
                        Type of worker instance for Dask cluster
  --scheduler_instance_type SCHEDULER_INSTANCE_TYPE
                        Type of scheduler instance for Dask cluster
  --server_mode SERVER_MODE
                        Keep running after all ligands have been processed
  --failed_ligand_out FAILED_LIGAND_OUT
                        Output file containing failed ligand filenames (.csv)
  --error_msg_out ERROR_MSG_OUT
                        Output file containing error messages that come from
                        docking engine (.txt)
  --errors_aws ERRORS_AWS
                        Output file containing error messages that come from
                        AWS (.txt)
  --restart RESTART     Run leftover unprocessed files
  --cost_per_cpu COST_PER_CPU
                        Cost per AWS CPU
  --debug DEBUG         Write debug files (for development only)
  --local LOCAL         Run dockingfactory in local mode
```

### Waiting for the script to finish

The script prints lines, one line per second, with the current statistics, for example:
```
3675/245/0/12223 clusters: 1, workers: 2, CPUs: 128, Elapsed: 27 min 04 s, Left: 62 min, Rate: 2.26 lig/sec, Current cost: $1.54, Cost estimate: $6.14
```
Here, 3675 is the number of processed ligands (both successes and failures), 245 is the number of failures, and 12223 is the total number of ligands. The zero is the number of ligands that have failed due to technical reason.

As soon as all ligands are processed, the script terminates (unless you specified `--server_mode=true`).


## Configuration File

You can have a YAML configuration file, or specify parameters as the script’s command line arguments, or both. Command line arguments take precedence over configuration file.

### Example

Example `config.yaml`:

```
address: http://10.2.34.23:8000
maximum_scale: 1
name: cluster-arm
partition: compute-cpu
worker_instance_type: c6g.16xlarge
scheduler_instance_type: c6g.medium

handler: smina
handler_config: /home/username/docking/dockingfactory/ZINC/smina_zinc.txt
input_path: /home/username/docking/dockingfactory/ZINC/viva_VFVS_100
receptor: /home/userame/docking/dockingfactory/ZINC/receptor/AR_5JJ_Bside_protonated.pdbqt
output: /home/username/docking/dockingfactory/ZINC/zinc_out
```

## License

Quantori DockingFactory is released under [Apache License, Version 2.0](LICENSE.md)

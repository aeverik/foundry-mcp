# Overview of Foundry Binaries

This document provides a comprehensive overview of the binaries provided by the Foundry project, their purposes, and how to obtain them. It also includes commands, subcommands, use cases, and examples for each binary.

## Foundry Binaries

### Anvil

**Purpose**: Anvil is a tool for ...
**Commands**:
- `A fast local Ethereum development node`
- `Commands:`
- `completions        Generate shell completions script [aliases: com]`
- `generate-fig-spec  Generate Fig autocompletion spec [aliases: fig]`
- `help               Print this message or the help of the given subcommand(s)`
- `Number of dev accounts to generate and configure`
- `[default: 10]`
- `Block time in seconds for interval mining`
- `[aliases: blockTime]`
- `The balance of every dev account in Ether`
- `[default: 10000]`
- `Writes output of `anvil` as json to user-specified file`
- `Sets the derivation path of the child key to be derived.`
- `[default: m/44'/60'/0'/0/]`
- `Dump the state and block environment of chain on exit to the given file.`
- `If the value is a directory, the state will be written to `<VALUE>/state.json`.`
- `Print help (see a summary with '-h')`
- `The EVM hardfork to use.`
- `Choose the hardfork by name, e.g. `cancun`, `shanghai`, `paris`, `london`, etc... [default:`
- `latest]`
- `Initialize the genesis block with the given `genesis.json` file`
- `Launch an ipc server at the given path or default path = `/tmp/anvil.ipc``
- `[aliases: ipcpath]`
- `Number of threads to use. Specifying 0 defaults to the number of logical cores`
- `[aliases: jobs]`
- `Initialize the chain from a previously saved state snapshot`
- `BIP39 mnemonic phrase used for generating accounts. Cannot be used if `mnemonic_random` or`
- ``mnemonic_seed` are used`
- `Max number of states to persist on disk.`
- `Note that `prune_history` will overwrite `max_persisted_states` to 0.`
- `[aliases: mixed-mining]`
- `Automatically generates a BIP39 mnemonic phrase, and derives accounts from it. Cannot be used`
- `with other `mnemonic` options. You can specify the number of words you want in the mnemonic.`
- `[default: 12]`
- `Generates a BIP39 mnemonic phrase from a given seed Cannot be used with other `mnemonic` options.`
- `CAREFUL: This is NOT SAFE and should only be used for testing. Never use the private keys`
- `generated in production.`
- `Disable auto and interval mining, and mine on demand instead`
- `[aliases: no-mine]`
- `How transactions are sorted in the mempool`
- `[default: fees]`
- `Port number to listen on`
- `[default: 8545]`
- `Preserve historical state snapshots when dumping the state.`
- `This will save the in-memory states of the chain at particular block hashes.`
- `These historical states will be loaded into the memory when `--load-state` / `--state`, and aids`
- `in RPC calls beyond the block at which state was dumped.`
- `Don't keep full chain history. If a number argument is specified, at most this number of states`
- `is kept in memory.`
- `If enabled, no state will be persisted on disk, so `max_persisted_states` will be 0.`
- `Interval in seconds at which the state and block environment is to be dumped to disk.`
- `See --state and --dump-state`
- `Slots in an epoch`
- `[default: 32]`
- `This is an alias for both --load-state and --dump-state.`
- `It initializes the chain with the state and block environment stored at the file, if it exists,`
- `and dumps the chain's state on exit.`
- `The timestamp of the genesis block`
- `Number of blocks with transactions to keep in memory`
- `Print version`
- `Display options:`
- `The color of the log messages`
- `Possible values:`
- `Format log messages as JSON`
- `Do not print log messages`
- `Verbosity level of the log messages.`
- `Pass multiple times to increase the verbosity (e.g. -v, -vv, -vvv).`
- `Depending on the context the verbosity levels have different meanings.`
- `For example, the verbosity levels of the EVM are:`
- `Server options:`
- `The cors `allow_origin` header`
- `[default: *]`
- `Path to the cache directory where states are stored`
- `The hosts the server will listen on`
- `[env: ANVIL_IP_ADDR=]`
- `[default: 127.0.0.1]`
- `Disable CORS`
- `Disable the default request body size limit. At time of writing the default limit is 2MB`
- `Fork config:`
- `Sets the number of assumed available compute units per second for this provider`
- `default value: 330`
- `See also --fork-url and`
- `<https://docs.alchemy.com/reference/compute-units#what-are-cups-compute-units-per-second>`
- `Fetch state over a remote endpoint instead of starting from an empty state.`
- `If you want to fetch state from a specific block number, add a block number like`
- ``http://localhost:8545@1400000` or use the `--fork-block-number` argument.`
- `[aliases: rpc-url]`
- `Fetch state from a specific block number over a remote endpoint.`
- `See --fork-url.`
- `Specify chain id to skip fetching it from remote endpoint. This enables offline-start mode.`
- `You still must pass both `--fork-url` and `--fork-block-number`, and already have your required`
- `state cached on disk, anything missing locally would be fetched from the remote.`
- `Headers to use for the rpc client, e.g. "User-Agent: test-agent"`
- `See --fork-url.`
- `Initial retry backoff on encountering errors.`
- `See --fork-url.`
- `Fetch state from a specific transaction hash over a remote endpoint.`
- `See --fork-url.`
- `Disables rate limiting for this node's provider.`
- `default value: false`
- `See also --fork-url and`
- `<https://docs.alchemy.com/reference/compute-units#what-are-cups-compute-units-per-second>`
- `[aliases: no-rpc-rate-limit]`
- `Explicitly disables the use of RPC caching.`
- `All storage slots are read entirely from the endpoint.`
- `This flag overrides the project's configuration file.`
- `See --fork-url.`
- `Number of retry requests for spurious networks (timed out requests)`
- `Default value 5`
- `Timeout in ms for requests sent to remote JSON-RPC server in forking mode.`
- `Default value 45000`
- `Environment config:`
- `The base fee in a block`
- `[aliases: base-fee]`
- `The chain ID`
- `EIP-170: Contract code size limit in bytes. Useful to increase this because of tests. To disable`
- `entirely, use `--disable-code-size-limit`. By default, it is 0x6000 (~25kb)`
- `Disable the `call.gas_limit <= block.gas_limit` constraint`
- `Disable EIP-170: Contract code size limit`
- `Disable the enforcement of a minimum suggested priority fee`
- `[aliases: no-priority-fee]`
- `The block gas limit`
- `The gas price`
- `EVM options:`
- `Enables automatic impersonation on startup. This allows any transaction sender to be simulated as`
- `different accounts, which is useful for testing contract behavior`
- `[aliases: auto-unlock]`
- `Disable printing of `console.log` invocations to stdout`
- `[aliases: no-console-log]`
- `Disable the default create2 deployer`
- `[aliases: no-create2]`
- `The memory limit per EVM execution in bytes`
- `Enable Odyssey features`
- `Run an Optimism chain`
- `[aliases: optimism]`
- `Enable steps tracing used for debug calls returning geth-style traces`
- `[aliases: tracing]`
**Use Cases**:
- Example use case 1
- Example use case 2

### Forge

**Purpose**: Forge is a tool for ...
**Commands**:
- `Build, test, fuzz, debug and deploy Solidity contracts`
- `Commands:`
- `bind               Generate Rust bindings for smart contracts`
- `bind-json          Generate bindings for serialization/deserialization of project structs via JSON`
- `cheatcodes`
- `build              Build the project's smart contracts [aliases: b, compile]`
- `cache              Manage the Foundry cache`
- `clean              Remove the build artifacts and cache directories [aliases: cl]`
- `clone              Clone a contract from Etherscan`
- `compiler           Compiler utilities`
- `completions        Generate shell completions script [aliases: com]`
- `config             Display the current config [aliases: co]`
- `coverage           Generate coverage reports`
- `create             Deploy a smart contract [aliases: c]`
- `doc                Generate documentation for the project`
- `eip712             Generate EIP-712 struct encodings for structs from a given file`
- `flatten            Flatten a source file and all of its imports into one file [aliases: f]`
- `fmt                Format Solidity source files`
- `geiger             Detects usage of unsafe cheat codes in a project and its dependencies`
- `generate           Generate scaffold files`
- `generate-fig-spec  Generate Fig autocompletion spec [aliases: fig]`
- `help               Print this message or the help of the given subcommand(s)`
- `init               Create a new Forge project`
- `inspect            Get specialized information about a smart contract [aliases: in]`
- `install            Install one or multiple dependencies [aliases: i]`
- `remappings         Get the automatically inferred remappings for the project [aliases: re]`
- `remove             Remove one or multiple dependencies [aliases: rm]`
- `script             Run a smart contract as a script, building transactions that can be sent onchain`
- `selectors          Function selector utilities [aliases: se]`
- `snapshot           Create a gas snapshot of each test's gas usage [aliases: s]`
- `soldeer            Soldeer dependency manager`
- `test               Run the project's tests [aliases: t]`
- `tree               Display a tree visualization of the project's dependency graph [aliases: tr]`
- `update             Update one or multiple dependencies [aliases: u]`
- `verify-bytecode    Verify the deployed bytecode against its source on Etherscan [aliases: vb]`
- `verify-check       Check verification status on Etherscan [aliases: vc]`
- `verify-contract    Verify smart contracts on Etherscan [aliases: v]`
- `Print help (see a summary with '-h')`
- `Number of threads to use. Specifying 0 defaults to the number of logical cores`
- `[aliases: jobs]`
- `Print version`
- `Display options:`
- `The color of the log messages`
- `Possible values:`
- `Format log messages as JSON`
- `Do not print log messages`
- `Verbosity level of the log messages.`
- `Pass multiple times to increase the verbosity (e.g. -v, -vv, -vvv).`
- `Depending on the context the verbosity levels have different meanings.`
- `For example, the verbosity levels of the EVM are:`
- `Find more information in the book: http://book.getfoundry.sh/reference/forge/forge.html`
**Use Cases**:
- Example use case 1
- Example use case 2

### Cast

**Purpose**: Cast is a tool for ...
**Commands**:
- `A Swiss Army knife for interacting with Ethereum applications from the command line`
- `Commands:`
- `4byte                  Get the function signatures for the given selector from <https://openchain.xyz>`
- `[aliases: 4, 4b]`
- `4byte-calldata         Decode ABI-encoded calldata using <https://openchain.xyz> [aliases: 4c, 4bc]`
- `4byte-event            Get the event signature for a given topic 0 from <https://openchain.xyz> [aliases:`
- `4e, 4be, topic0-event, t0e]`
- `abi-encode             ABI encode the given function argument, excluding the selector [aliases: ae]`
- `access-list            Create an access list for a transaction [aliases: ac, acl]`
- `address-zero           Prints the zero address [aliases: --address-zero, az]`
- `admin                  Fetch the EIP-1967 admin account [aliases: adm]`
- `age                    Get the timestamp of a block [aliases: a]`
- `artifact               Generate an artifact file, that can be used to deploy a contract locally [aliases:`
- `ar]`
- `balance                Get the balance of an account in wei [aliases: b]`
- `base-fee               Get the basefee of a block [aliases: ba, fee, basefee]`
- `bind                   Generate a rust binding from a given ABI [aliases: bi]`
- `block                  Get information about a block [aliases: bl]`
- `block-number           Get the latest block number [aliases: bn]`
- `call                   Perform a call on an account without publishing a transaction [aliases: c]`
- `calldata               ABI-encode a function with arguments [aliases: cd]`
- `chain                  Get the symbolic name of the current chain`
- `chain-id               Get the Ethereum chain ID [aliases: ci, cid]`
- `client                 Get the current client version [aliases: cl]`
- `code                   Get the runtime bytecode of a contract [aliases: co]`
- `codehash               Get the codehash for an account`
- `codesize               Get the runtime bytecode size of a contract [aliases: cs]`
- `completions            Generate shell completions script [aliases: com]`
- `compute-address        Compute the contract address from a given nonce and deployer address [aliases: ca]`
- `concat-hex             Concatenate hex strings [aliases: --concat-hex, ch]`
- `constructor-args       Display constructor arguments used for the contract initialization [aliases: cra]`
- `create2                Generate a deterministic contract address using CREATE2 [aliases: c2]`
- `creation-code          Download a contract creation code from Etherscan and RPC [aliases: cc]`
- `decode-abi             Decode ABI-encoded input or output data [aliases: abi-decode, --abi-decode, ad]`
- `decode-calldata        Decode ABI-encoded input data [aliases: calldata-decode, --calldata-decode, cdd]`
- `decode-eof             Decodes EOF container bytes`
- `decode-error           Decode custom error data [aliases: error-decode, --error-decode, erd]`
- `decode-event           Decode event data [aliases: event-decode, --event-decode, ed]`
- `decode-string          Decode ABI-encoded string [aliases: string-decode, --string-decode, sd]`
- `decode-transaction     Decodes a raw signed EIP 2718 typed transaction [aliases: dt, decode-tx]`
- `disassemble            Disassembles a hex-encoded bytecode into a human-readable representation [aliases:`
- `da]`
- `estimate               Estimate the gas cost of a transaction [aliases: e]`
- `find-block             Get the block number closest to the provided timestamp [aliases: f]`
- `format-bytes32-string  Formats a string into bytes32 encoding [aliases: --format-bytes32-string]`
- `format-units           Format a number from smallest unit to decimal with arbitrary decimals [aliases:`
- `from-bin               Convert binary data into hex data [aliases: --from-bin, from-binx, fb]`
- `from-fixed-point       Convert a fixed point number into an integer [aliases: --from-fix, ff]`
- `from-rlp               Decodes RLP hex-encoded data [aliases: --from-rlp]`
- `from-utf8              Convert UTF8 text to hex [aliases: --from-ascii, --from-utf8, from-ascii, fu, fa]`
- `from-wei               Convert wei into an ETH amount [aliases: --from-wei, fw]`
- `gas-price              Get the current gas price [aliases: g]`
- `generate-fig-spec      Generate Fig autocompletion spec [aliases: fig]`
- `hash-message           Hash a message according to EIP-191 [aliases: --hash-message, hm]`
- `hash-zero              Prints the zero hash [aliases: --hash-zero, hz]`
- `help                   Print this message or the help of the given subcommand(s)`
- `implementation         Fetch the EIP-1967 implementation for a contract Can read from the implementation`
- `slot or the beacon slot [aliases: impl]`
- `index                  Compute the storage slot for an entry in a mapping [aliases: in]`
- `index-erc7201          Compute storage slots as specified by `ERC-7201: Namespaced Storage Layout``
- `[aliases: index7201, in7201]`
- `interface              Generate a Solidity interface from a given ABI [aliases: i]`
- `keccak                 Hash arbitrary data using Keccak-256 [aliases: k, keccak256]`
- `logs                   Get logs by signature or topic [aliases: l]`
- `lookup-address         Perform an ENS reverse lookup [aliases: la]`
- `max-int                Prints the maximum value of the given integer type [aliases: --max-int, maxi]`
- `max-uint               Prints the maximum value of the given integer type [aliases: --max-uint, maxu]`
- `min-int                Prints the minimum value of the given integer type [aliases: --min-int, mini]`
- `mktx                   Build and sign a transaction [aliases: m]`
- `namehash               Calculate the ENS namehash of a name [aliases: na, nh]`
- `nonce                  Get the nonce for an account [aliases: n]`
- `parse-bytes32-address  Parses a checksummed address from bytes32 encoding. [aliases:`
- `parse-bytes32-string   Parses a string from bytes32 encoding [aliases: --parse-bytes32-string]`
- `parse-units            Convert a number from decimal to smallest unit with arbitrary decimals [aliases:`
- `pretty-calldata        Pretty print calldata [aliases: pc]`
- `proof                  Generate a storage proof for a given storage slot [aliases: pr]`
- `publish                Publish a raw transaction to the network [aliases: p]`
- `receipt                Get the transaction receipt for a transaction [aliases: re]`
- `resolve-name           Perform an ENS lookup [aliases: rn]`
- `rpc                    Perform a raw JSON-RPC request [aliases: rp]`
- `run                    Runs a published transaction in a local environment and prints the trace [aliases:`
- `r]`
- `selectors              Extracts function selectors and arguments from bytecode [aliases: sel]`
- `send                   Sign and publish a transaction [aliases: s]`
- `shl                    Perform a left shifting operation`
- `shr                    Perform a right shifting operation`
- `sig                    Get the selector for a function [aliases: si]`
- `sig-event              Generate event signatures from event string [aliases: se]`
- `source                 Get the source code of a contract from a block explorer [aliases: et, src]`
- `storage                Get the raw value of a contract's storage slot [aliases: st]`
- `storage-root           Get the storage root for an account [aliases: sr]`
- `to-ascii               Convert hex data to an ASCII string [aliases: --to-ascii, tas, 2as]`
- `to-base                Converts a number of one base to another [aliases: --to-base, --to-radix,`
- `to-radix, tr, 2r]`
- `to-bytes32             Right-pads hex data to 32 bytes [aliases: --to-bytes32, tb, 2b]`
- `to-check-sum-address   Convert an address to a checksummed format (EIP-55) [aliases:`
- `to-dec                 Converts a number of one base to decimal [aliases: --to-dec, td, 2d]`
- `to-fixed-point         Convert an integer into a fixed point number [aliases: --to-fix, tf, 2f]`
- `to-hex                 Converts a number of one base to another [aliases: --to-hex, th, 2h]`
- `to-hexdata             Normalize the input to lowercase, 0x-prefixed hex [aliases: --to-hexdata, thd,`
- `2hd]`
- `to-int256              Convert a number to a hex-encoded int256 [aliases: --to-int256, ti, 2i]`
- `to-rlp                 RLP encodes hex data, or an array of hex data [aliases: --to-rlp]`
- `to-uint256             Convert a number to a hex-encoded uint256 [aliases: --to-uint256, tu, 2u]`
- `to-unit                Convert an ETH amount into another unit (ether, gwei or wei) [aliases: --to-unit,`
- `tun, 2un]`
- `to-utf8                Convert hex data to a utf-8 string [aliases: --to-utf8, tu8, 2u8]`
- `to-wei                 Convert an ETH amount to wei [aliases: --to-wei, tw, 2w]`
- `tx                     Get information about a transaction [aliases: t]`
- `tx-pool                Inspect the TxPool of a node [aliases: tp]`
- `upload-signature       Upload the given signatures to <https://openchain.xyz> [aliases: ups]`
- `wallet                 Wallet management utilities [aliases: w]`
- `Print help (see a summary with '-h')`
- `Number of threads to use. Specifying 0 defaults to the number of logical cores`
- `[aliases: jobs]`
- `Print version`
- `Display options:`
- `The color of the log messages`
- `Possible values:`
- `Format log messages as JSON`
- `Do not print log messages`
- `Verbosity level of the log messages.`
- `Pass multiple times to increase the verbosity (e.g. -v, -vv, -vvv).`
- `Depending on the context the verbosity levels have different meanings.`
- `For example, the verbosity levels of the EVM are:`
- `Find more information in the book: http://book.getfoundry.sh/reference/cast/cast.html`
**Use Cases**:
- Example use case 1
- Example use case 2

### Chisel

**Purpose**: Chisel is a tool for ...
**Commands**:
- `Fast, utilitarian, and verbose Solidity REPL`
- `Commands:`
- `list         List all cached sessions`
- `load         Load a cached session`
- `view         View the source of a cached session`
- `clear-cache  Clear all cached chisel sessions from the cache directory`
- `eval         Simple evaluation of a command without entering the REPL`
- `help         Print this message or the help of the given subcommand(s)`
- `Number of threads to use. Specifying 0 defaults to the number of logical cores`
- `[aliases: jobs]`
- `Print help (see a summary with '-h')`
- `Print version`
- `Display options:`
- `Verbosity level of the log messages.`
- `Pass multiple times to increase the verbosity (e.g. -v, -vv, -vvv).`
- `Depending on the context the verbosity levels have different meanings.`
- `For example, the verbosity levels of the EVM are:`
- `Do not print log messages`
- `Format log messages as JSON`
- `The color of the log messages`
- `Possible values:`
- `REPL options:`
- `Path to a directory containing Solidity files to import, or path to a single Solidity file.`
- `These files will be evaluated before the top-level of the REPL, therefore functioning as a`
- `prelude`
- `Disable the default `Vm` import.`
- `The import is disabled by default if the Solc version is less than 0.6.2.`
- `Cache options:`
- `Clear the cache and artifacts folder and recompile`
- `Build options:`
- `Disable the cache`
- `Whether to compile contracts to EOF bytecode`
- `Skip building files whose names contain the given filter.`
- ``test` and `script` are aliases for `.t.sol` and `.s.sol`.`
- `Linker options:`
- `Set pre-linked libraries`
- `[env: DAPP_LIBRARIES=]`
- `Compiler options:`
- `Ignore solc warnings by error code`
- `Warnings will trigger a compiler error`
- `Do not auto-detect the `solc` version`
- `Specify the solc version, or a path to a local solc, to build with.`
- `Valid values are in the format `x.y.z`, `solc:x.y.z` or `path/to/solc`.`
- `Do not access the network.`
- `Missing solc versions will not be installed.`
- `Use the Yul intermediate representation compilation pipeline`
- `Changes compilation to only use literal content and not URLs`
- `Do not append any metadata to the bytecode.`
- `This is equivalent to setting `bytecode_hash` to `none` and `cbor_metadata` to `false`.`
- `Includes the AST as JSON in the compiler output`
- `The target EVM version`
- `Activate the Solidity optimizer`
- `[possible values: true, false]`
- `The number of runs specifies roughly how often each opcode of the deployed code will be executed`
- `across the life-time of the contract. This means it is a trade-off parameter between code size`
- `(deploy cost) and code execution cost (cost after deployment). An `optimizer_runs` parameter of`
- ``1` will produce short but expensive code. In contrast, a larger `optimizer_runs` parameter will`
- `produce longer but more gas efficient code`
- `Extra output to include in the contract's artifact.`
- `Example keys: evm.assembly, ewasm, ir, irOptimized, metadata`
- `For a full description, see`
- `<https://docs.soliditylang.org/en/v0.8.13/using-the-compiler.html#input-description>`
- `Extra output to write to separate files.`
- `Valid values: metadata, ir, irOptimized, ewasm, evm.assembly`
- `Project options:`
- `The path to the contract artifacts folder`
- `Revert string configuration.`
- `Possible values are "default", "strip" (remove), "debug" (Solidity-generated revert strings) and`
- `"verboseDebug"`
- `Generate build info files`
- `Output path to directory that build info files will be written to`
- `The project's root path.`
- `By default root of the Git repository, if in one, or the current working directory.`
- `The contracts source directory`
- `The project's remappings`
- `The project's remappings from the environment`
- `The path to the compiler cache`
- `The path to the library folder`
- `Use the Hardhat-style project layout.`
- `This is the same as using: `--contracts contracts --lib-paths node_modules`.`
- `[aliases: hh]`
- `Path to the config file`
- `EVM options:`
- `Fetch state over a remote endpoint instead of starting from an empty state.`
- `If you want to fetch state from a specific block number, see --fork-block-number.`
- `[aliases: rpc-url]`
- `Fetch state from a specific block number over a remote endpoint.`
- `See --fork-url.`
- `Number of retries.`
- `See --fork-url.`
- `Initial retry backoff on encountering errors.`
- `See --fork-url.`
- `Explicitly disables the use of RPC caching.`
- `All storage slots are read entirely from the endpoint.`
- `This flag overrides the project's configuration file.`
- `See --fork-url.`
- `The initial balance of deployed test contracts`
- `The address which will be executing tests/scripts`
- `Enable the FFI cheatcode`
- `Use the create 2 factory in all cases including tests and non-broadcasting scripts`
- `The CREATE2 deployer address to use, this will override the one in the config`
- `Fork config:`
- `Sets the number of assumed available compute units per second for this provider`
- `default value: 330`
- `See also --fork-url and`
- `<https://docs.alchemy.com/reference/compute-units#what-are-cups-compute-units-per-second>`
- `Disables rate limiting for this node's provider.`
- `See also --fork-url and`
- `<https://docs.alchemy.com/reference/compute-units#what-are-cups-compute-units-per-second>`
- `[aliases: no-rate-limit]`
- `Executor environment config:`
- `EIP-170: Contract code size limit in bytes. Useful to increase this because of tests. By default,`
- `it is 0x6000 (~25kb)`
- `The chain name or EIP-155 chain ID`
- `[aliases: chain-id]`
- `The gas price`
- `The base fee in a block`
- `[aliases: base-fee]`
- `The transaction origin`
- `The coinbase of the block`
- `The timestamp of the block`
- `The block number`
- `The block difficulty`
- `The block prevrandao value. NOTE: Before merge this field was mix_hash`
- `The block gas limit`
- `[aliases: gas-limit]`
- `The memory limit per EVM execution in bytes. If this limit is exceeded, a `MemoryLimitOOG` result`
- `is thrown.`
- `The default is 128MiB.`
- `Whether to disable the block gas limit checks`
- `[aliases: no-gas-limit]`
- `Whether to enable isolation of calls. In isolation mode all top-level calls are executed as a`
- `separate transaction in a separate EVM context, enabling more precise gas accounting and`
- `transaction state changes`
- `Whether to enable Odyssey features`
**Use Cases**:
- Example use case 1
- Example use case 2

### Example Use Cases

#### Anvil
- **Simulating Ethereum Transactions**: Use `anvil` to simulate Ethereum transactions locally. For example, start a local Ethereum node with `anvil start` and test smart contract interactions.
- **Testing Gas Costs**: Deploy contracts to the local node and measure gas costs for various operations.

#### Forge
- **Writing and Running Tests**: Write Solidity tests using the Forge Standard Library and run them with `forge test`.
- **Deploying Contracts**: Use `forge create` to deploy contracts to a local or remote Ethereum network.
- **Gas Optimization**: Analyze gas usage with `forge snapshot` and optimize contract functions.

#### Cast
- **Interacting with Deployed Contracts**: Use `cast call` to invoke functions on deployed contracts.
- **Querying Blockchain Data**: Retrieve account balances with `cast balance` or fetch block details with `cast block`.
- **Sending Transactions**: Use `cast send` to send transactions to the Ethereum network.

#### Chisel
- **Managing Dependencies**: Use `chisel init` to set up a new project and `chisel install` to add dependencies.
- **Advanced Workflows**: Automate complex workflows with `chisel eval` and manage project configurations.

#### General
- **Forking Mainnet**: Use `anvil` and `cast` to fork the Ethereum mainnet and test contracts in a realistic environment.
- **Deterministic Deployments**: Leverage `forge` and `cast` to perform deterministic deployments using CREATE2.
- **Debugging**: Use `forge debug` to step through contract execution and identify issues.

## How to Obtain Foundry Binaries

The Foundry binaries can be obtained using the `foundryup` tool, which ensures you always have the latest stable version. To install Foundry, run the following command:

```bash
curl -L https://foundry.paradigm.xyz | bash
```

After installation, you can update Foundry to the latest stable version by running:

```bash
foundryup
```

This will install or update the Foundry binaries (`forge`, `cast`, `anvil`, and `chisel`) to the latest stable version.

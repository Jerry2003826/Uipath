from permitops_worker.cli import build_parser


def test_cli_exposes_v11_live_swarm_local_command():
    parser = build_parser()

    args = parser.parse_args(["v11-live-swarm-local"])

    assert args.func.__name__ == "cmd_v11_live_swarm_local"

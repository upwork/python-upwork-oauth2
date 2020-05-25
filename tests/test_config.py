from upwork import config


def test_config_initialization():
    cfg = config.Config(
        {
            "client_id": "keyxxxxxxxxxxxxxxxxxxxx",
            "client_secret": "secretxxxxxxxxxx",
            "redirect_uri": "https://a.callback.url",
            "token": {"access_token": "a"},
        }
    )

    assert cfg.client_id == "keyxxxxxxxxxxxxxxxxxxxx"
    assert cfg.client_secret == "secretxxxxxxxxxx"
    assert cfg.redirect_uri == "https://a.callback.url"
    assert cfg.token == {"access_token": "a"}

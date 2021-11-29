[![Pipeline status][pipeline-status]][commits]
[![Coverage report][coverage-report]][commits]
[![Pylint score][pylint-score]][pylint-log]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <p>
    <a href="https://git.yodabyte.ch/black-fennec/black-fennec">
      <img src="docs/source/images/corporate_identity/logo.jpg" alt="Logo" width="50%">
    </a>
  </p>
  <p align="center">
    bring structure for chaos
    <br />
    <a href="https://git.yodabyte.ch/black-fennec/black-fennec"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://git.yodabyte.ch/black-fennec/black-fennec/issues">Report Bug</a>
    ·
    <a href="https://git.yodabyte.ch/black-fennec/black-fennec/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->

## Table of Contents

* [About the Project](#about-the-project)
    * [Built With](#built-with)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)

<!-- ABOUT THE PROJECT -->

## About The Project

[![Black-Fennec Screen Shot][product-screenshot]](docs/source/images/corporate_identity/demo/ui.png)

Black Fennec is going to be an application that is able to manage unstructured data by interpreting information
compositions known to its type system. These interpretations are then visualised. The type system in its nature is a
weak typed dynamic object model that can be extended easily. To support specialised use cases and allow rapid
development Black Fennec provides an extension api. With the final product one will be capable of visualising and
editing any JSON and YAML files in a more productive way. A close integration of git allows for collaboration and data
sharing over existing infrastructure.

### Built With

* [GTK3](https://docs.gtk.org/gtk3/)

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple example steps.

In the near future a flatpak installation will be provided.

### Prerequisites

To run Black-Fennec one needs python 3.8 installed on the computer.

### Installation

1. Clone the repo

```sh
git clone https://git.yodabyte.ch/black-fennec/black-fennec.git
```

2. Install OS-level Dependencies

```sh
sudo dnf install python3-devel cairo cairo-devel gobject-introspection-devel cairo-gobject-devel
```

3. Install PIP packages

```sh
pip install -r requirements.txt
```

### Usage

To run Black-Fennec the main has to be executed with python.

```sh
python black_fennec.py
```

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://git.yodabyte.ch/black-fennec/black-fennec/issues) for a list of proposed features (and
known issues).

<!-- CONTRIBUTING -->

## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the GNU General Public License. See `LICENSE` for more information.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[pipeline-status]: https://git.yodabyte.ch/black-fennec/black-fennec/badges/dev/pipeline.svg

[coverage-report]: https://git.yodabyte.ch/black-fennec/black-fennec/badges/dev/coverage.svg

[pylint-score]: https://git.yodabyte.ch/black-fennec/black-fennec/-/jobs/artifacts/dev/raw/pylint/pylint.svg?job=run%20linter

[pylint-log]: https://git.yodabyte.ch/black-fennec/black-fennec/-/jobs/artifacts/dev/raw/pylint/pylint.log?job=run%20linter

[commits]: https://git.yodabyte.ch/black-fennec/black-fennec/-/commits/dev

[issues-url]: https://git.yodabyte.ch/black-fennec/black-fennec/issues

[product-screenshot]: docs/source/images/corporate_identity/demo/ui.png

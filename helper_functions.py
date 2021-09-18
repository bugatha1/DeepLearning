{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "helper_functions.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNBveDmaaqXfi2/vCpuhXXw",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/bugatha1/tensorflow-deep-learning/blob/main/helper_functions.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "n7_oBqgiHbia",
        "outputId": "ae60de4e-4bd3-4a3b-c0ec-1f59f71d6432"
      },
      "source": [
        "import tensorflow as tf\n",
        "\n",
        "tf.__version__"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'2.6.0'"
            ]
          },
          "metadata": {},
          "execution_count": 2
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iAui1QiLHu8H"
      },
      "source": [
        "# Create function to unzip a zipfile into current working directory \n",
        "# (since we're going to be downloading and unzipping a few files)\n",
        "\n",
        "import zipfile\n",
        "\n",
        "def unzip_data(filename):\n",
        "  zip_ref = zipfile.zipFile(filename, 'r')\n",
        "  zip_ref.extractall()\n",
        "  zip_ref.close()"
      ],
      "execution_count": 3,
      "outputs": []
    }
  ]
}
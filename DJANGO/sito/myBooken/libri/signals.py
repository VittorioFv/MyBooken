import os


def ImmaginiLibriCleanup(sender, instance, using, **kwargs):
    if instance.immagine:
        if os.path.isfile(instance.immagine.path):
            os.remove(instance.immagine.path)

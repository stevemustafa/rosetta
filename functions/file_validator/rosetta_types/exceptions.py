
# define custom errors

class FileTypeIncorrect(Exception):
    def __init__(self, file_extension):
        self.acceptable_file_types = ['mp3', 'mp4', 'ogg', 'flac', 'webm', 'amr', 'wav']
        self.file_extension = file_extension
        self.message = "Invalid file type provided: '{}'\nFile should be any of type: '{}'"\
            .format(self.file_extension, self.acceptable_file_types)
        super().__init__(self.message)

class FileTooLarge(Exception):
    def __init__(self, file_size):
        self.file_size = file_size
        self.max_file_size = 2147483648
        self.message = "Invalid file size:  'file provided '{}' is too big.  Max filesize is '{}'"\
            .format(self.file_size, self.max_file_size)
        super().__init__(self.message)
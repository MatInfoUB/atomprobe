import struct


class Specimen:

    def __init__(self, name=None):

        """
        Defines an atomprobe specimen.
        The current functionality allows you to obtain
        its parameters from an epos or a pos file
        """
        if name is not None:
            self.name = name


    def from_epos_file(self, filename=None):

        """
        :param filename:
        :return: List of parameters that define a reconstructed
                       atomprobe specimen
        """
        if filename is None:
            raise ValueError('Need a Filename to import')

        n = len(file(filename, 'rb').read()) / 4 # Number of variables to be imported
        num_atoms = n / 11  # Number of atoms in the dataset
        format_specifier = '>' + 'fffffffffII' * num_atoms

        if struct.calcsize(format_specifier) != 4 * n:
            return False

        total_data = struct.unpack(format_specifier, file(filename, 'rb').read(4 * n))

        self.x = total_data[::11]
        self.y = total_data[1::11]
        self.z = total_data[2::11]
        self.mass_to_charge = total_data[3::11]
        self.time_of_filght = total_data[4::11]
        self.DC_volt = total_data[5::11]
        self.pulse_voltage = total_data[6::11]
        self.det_x = total_data[7::11]
        self.det_y = total_data[8::11]
        self.pulse = total_data[9::11]
        self.ions_per_pulse = total_data[10::11]

    def from_pos_file(self, filename):

        """
                :param filename:
                :return: List of parameters that define a reconstructed
                               atomprobe specimen
                """
        if filename is None:
            raise ValueError('Need a Filename to import')

        n = len(file(filename, 'rb').read()) / 4  # Number of variables to be imported
        num_atoms = n / 4  # Number of atoms in the dataset
        format_specifier = '>' + 'f' * num_atoms

        if struct.calcsize(format_specifier) != 4 * n:
            return False

        total_data = struct.unpack(format_specifier, file(filename, 'rb').read(4 * n))

        self.x = total_data[::11]
        self.y = total_data[1::11]
        self.z = total_data[2::11]
        self.mass_to_charge = total_data[3::11]

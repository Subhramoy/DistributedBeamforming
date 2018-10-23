/* -*- c++ -*- */
/*
 * Copyright 2018 GENESYS Lab..
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_BEAMFORMING_PAYLOAD_GENERATOR_CPP_IMPL_H
#define INCLUDED_BEAMFORMING_PAYLOAD_GENERATOR_CPP_IMPL_H

#include <beamforming/payload_generator_cpp.h>

namespace gr {
  namespace beamforming {

    class payload_generator_cpp_impl : public payload_generator_cpp
    {
     private:
      void initialize_mod_information();
      int payload_size_multiplier = 1;
      std::vector <struct modulation*> mods;


     public:
      payload_generator_cpp_impl(std::string file_path ,  int size = 1);
      ~payload_generator_cpp_impl();

      // Created function to calculate payload
      void generate_pdu();
      void generate_pdu(pmt::pmt_t msg);

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };


    struct modulation {
      std::string name;
      int number_of_symbols;
      const unsigned char* payload_ptr;
    };



    // 48 Bytes of data containing 64 different 6-bit symbols
    const unsigned char payload_64QAM[] = {0, 16, 131, 16, 81, 135, 32, 146,
                                    139, 48, 211, 143, 65, 20, 147, 81,
                                    85, 151, 97, 150, 155, 113, 215, 159,
                                    130, 24, 163, 146, 89,167, 162, 154,
                                    171, 178, 219, 175, 195, 28, 179, 211,
                                    93, 183, 227, 158, 187, 243, 223, 191};



    // 20 Bytes of data containing 32 different 5-bit symbols
     const unsigned char payload_32QAM[] = {0, 68, 50, 20, 199, 66, 84, 182,
                                            53, 207, 132, 101, 58, 86, 215, 198,
                                            117, 190, 119, 223 };

    // 8 Bytes of data containing 16 different 4-bit symbols
     const unsigned char payload_16QAM[] = {1, 35, 69, 103, 137, 171, 205, 239};


    // 3 Bytes of data containing 8 different 3-bit symbols
     const unsigned char payload_8QAM[] = {5, 57, 119};

     // 1 Bytes of data containing 4 different 2-bit symbols
      const unsigned char payload_QPSK[] = {27};


  } // namespace beamforming
} // namespace gr

#endif /* INCLUDED_BEAMFORMING_PAYLOAD_GENERATOR_CPP_IMPL_H */

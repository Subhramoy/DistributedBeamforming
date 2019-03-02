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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include <gnuradio/blocks/pdu.h>
#include "payload_generator_cpp_impl.h"

namespace gr {
  namespace beamforming {

    payload_generator_cpp::sptr
    payload_generator_cpp::make(std::string file_path , int size)
    {
      return gnuradio::get_initial_sptr
        (new payload_generator_cpp_impl( file_path,  size));
    }

    /*
     * The private constructor
     */
    payload_generator_cpp_impl::payload_generator_cpp_impl(std::string file_path , int size)
      : gr::block("payload_generator_cpp",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(0, 0, 0)
            )
    {

      if (size < 1) this->payload_size_multiplier = 1;
      else payload_size_multiplier = size;


      message_port_register_in(pmt::mp("generate"));

      message_port_register_out(pmt::mp("64QAM_pdu"));
      message_port_register_out(pmt::mp("32QAM_pdu"));
      message_port_register_out(pmt::mp("16QAM_pdu"));
      message_port_register_out(pmt::mp("8QAM_pdu"));
      message_port_register_out(pmt::mp("QPSK_pdu"));
      message_port_register_out(pmt::mp("BPSK_pdu"));


      set_msg_handler(pmt::mp("generate"), boost::bind(&payload_generator_cpp_impl::generate_pdu, this, _1));


      initialize_mod_information();



    }

    /*
     * Our virtual destructor.
     */
    payload_generator_cpp_impl::~payload_generator_cpp_impl()
    {
      this->mods.clear();
    }



    void
    payload_generator_cpp_impl::generate_pdu()
    {


      // std::cout<< "Generate_pdu handler called" <<std::endl;

      for(int i = 0; i < this->mods.size(); i++) {
        modulation* m = this->mods[i];

        // Calculating data size in bytes
        int size_in_bytes = m->number_of_symbols * (std::log(m->number_of_symbols)/std::log(2)) / 8 ;
        if(m->name == "BPSK" ) // Ugly coding to solve BPSK
          size_in_bytes = 8;

        /*
        std::cout << "Parsing the data for "
                  << m->name << " modulation:: Containing "
                  << size_in_bytes << " bytes"
                  << std::endl;
        */

        // Create the vector with the byte stream
        std::vector<unsigned char> t_vec( m->payload_ptr, m->payload_ptr+size_in_bytes);

        // Repeat the data to generate symbol arrays in same size (64 times size_multiplier)--- repmat() equvalient in MATLAB
        int loop_count = this->payload_size_multiplier *( 64 / m->number_of_symbols );

        //std::cout << loop_count << std::endl;

        for(int r = 1; r < loop_count; r++){
            t_vec.insert(t_vec.end(), m->payload_ptr,  m->payload_ptr+size_in_bytes);
        }

        /*
        std::cout << "Creating binary for "
                  << m->name
                  << " modulation:: Containing "
                  << t_vec.size() << " bytes"
                  << std::endl;
        */

        pmt::pmt_t vec_pmt(pmt::make_blob(&t_vec[0], t_vec.size()));
        pmt::pmt_t pdu(pmt::cons(pmt::PMT_NIL, vec_pmt));

        // Send out pdu throught corresponding message port
        message_port_pub( pmt::mp(m->name + "_pdu"), pdu);
      }


    }

    // UNUSED function
    void
    payload_generator_cpp_impl::generate_pdu(pmt::pmt_t msg)
    {
      payload_generator_cpp_impl::generate_pdu();
    }


    /* IMPORTANT! Following functions should not be used, since this block is not supposed to get any inputs */
    void
    payload_generator_cpp_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
      std::cout<< "This function should not be called";
    }

    int
    payload_generator_cpp_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
    //  const <+ITYPE+> *in = (const <+ITYPE+> *) input_items[0];
    //  <+OTYPE+> *out = (<+OTYPE+> *) output_items[0];

      std::cout<< "This function should not be called";
      // Do <+signal processing+>
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }



    // Generate modulations and related payloads
    void
      payload_generator_cpp_impl::initialize_mod_information(){

      // 64QAM
      struct modulation* mod_64qam = new struct modulation;
      mod_64qam->name = "64QAM";
      mod_64qam->number_of_symbols = 64;
      mod_64qam->payload_ptr = payload_64QAM;
      this->mods.push_back(mod_64qam);


      // 32QAM
      struct modulation* mod_32qam = new struct modulation;
      mod_32qam->name = "32QAM";
      mod_32qam->number_of_symbols = 32;
      mod_32qam->payload_ptr = payload_32QAM;
      this->mods.push_back(mod_32qam);


      // 16QAM
      struct modulation* mod_16qam = new struct modulation;
      mod_16qam->name = "16QAM";
      mod_16qam->number_of_symbols = 16;
      mod_16qam->payload_ptr = payload_16QAM;
      this->mods.push_back(mod_16qam);

      // 8QAM
      struct modulation* mod_8qam = new struct modulation;
      mod_8qam->name = "8QAM";
      mod_8qam->number_of_symbols = 8;
      mod_8qam->payload_ptr = payload_8QAM;
      this->mods.push_back(mod_8qam);


      // QPSK
      struct modulation* mod_qpsk = new struct modulation;
      mod_qpsk->name = "QPSK";
      mod_qpsk->number_of_symbols = 4;
      mod_qpsk->payload_ptr = payload_QPSK;
      this->mods.push_back(mod_qpsk);



      // BPSK
     struct modulation* mod_bpsk = new struct modulation;
      mod_bpsk->name = "BPSK";
//    mod_bpsk->number_of_symbols = 2;
      mod_bpsk->number_of_symbols = 64;
      mod_bpsk->payload_ptr = payload_BPSK;
      this->mods.push_back(mod_bpsk);


    }



  } /* namespace beamforming */
} /* namespace gr */
